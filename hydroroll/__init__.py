from collections import defaultdict
from itertools import chain
from pathlib import Path
from typing import Dict, List, Optional, Type, Union
from iamai import ConfigModel, Plugin
from iamai.log import logger, error_or_exception
from iamai.utils import ModulePathFinder, get_classes_from_module_name, get_classes_from_dir, get_classes_from_module
from .config import GlobalConfig
from iamai.exceptions import LoadModuleError
from .utils import BasePlugin, RegexPluginBase, CommandPluginBase
import os
# from .core import Rule, RuleLoadType
from HydroRollCore import Rule, RuleLoadType

class HydroRoll(Plugin):
    
    class Config(ConfigModel):
        __config_name__ = "HydroRoll"
    
    priority = 0
    rules_priority_dict: Dict[int, List[Type[Rule]]] = defaultdict(list)
    _module_path_finder = ModulePathFinder()
    
    
    def _load_rule_class(
        self,
        rule_class: Type[Rule],
        rule_load_type: RuleLoadType,
        rule_file_path: Optional[str],
    ):
        logger.info(f'Loading rule from class "{rule_class!r}"')
        """加载规则类。"""
        priority = getattr(rule_class, "priority", None)
        if type(priority) is int and priority >= 0:
            for _rule in self.rules:
                if _rule.__name__ == rule_class.__name__:
                    logger.warning(
                        f'Already have a same name rule "{_rule.__name__}"'
                    )
            rule_class.__rule_load_type__ = rule_load_type
            rule_class.__rule_file_path__ = rule_file_path
            self.rules_priority_dict[priority].append(rule_class)
            logger.success(
                f'Succeeded to load rule "{rule_class.__name__}" '
                f'from class "{rule_class!r}"'
            )
        else:
            error_or_exception(
                f'Load rule from class "{rule_class!r}" failed:',
                LoadModuleError(
                    f'Rule priority incorrect in the class "{rule_class!r}"'
                ),
                self.bot.config.bot.log.verbose_exception,
            )
    
    def _load_rules_from_module_name(
        self, module_name: str, rule_load_type: RuleLoadType
    ):
        logger.info(f'Loading rules from module "{module_name}"')
        """从模块名称中规则包模块。"""
        try:
            rule_classes = get_classes_from_module_name(module_name, Rule)
        except ImportError as e:
            error_or_exception(
                f'Import module "{module_name}" failed:',
                e,
                self.bot.config.bot.log.verbose_exception,
            )
        else:
            for rule_class, module in rule_classes:
                self._load_rule_class(
                    rule_class,
                    rule_load_type,
                    module.__file__,
                )

    def _load_rules(
        self,
        *rules: Union[Type[Plugin], str, Path],
        rule_load_type: Optional[RuleLoadType] = None,
    ):
        """加载规则包。

        Args:
            *rules: 规则类、规则包模块名称或者规则包模块文件路径。类型可以是 `Type[Rule]`, `str` 或 `pathlib.Path`。
                如果为 `Type[Rule]` 类型时，将作为规则类进行加载。
                如果为 `str` 类型时，将作为规则包模块名称进行加载，格式和 Python `import` 语句相同。
                    例如：`path.of.rule`。
                如果为 `pathlib.Path` 类型时，将作为规则包模块文件路径进行加载。
                    例如：`pathlib.Path("path/of/rule")`。
            rule_load_type: 规则加载类型，如果为 None 则自动判断，否则使用指定的类型。
        """
        logger.info("Loading rules...")
        for rule_ in rules:
            if isinstance(rule_, type):
                if issubclass(rule_, Rule):
                    self._load_rule_class(
                        rule_, rule_load_type or RuleLoadType.CLASS, None
                    )
                else:
                    logger.error(
                        f'The rule class "{rule_!r}" must be a subclass of Rule'
                    )
            elif isinstance(rule_, str):
                logger.warning(f'Loading rules from module "{rule_}"')
                self._load_rules_from_module_name(
                    rule_, rule_load_type or RuleLoadType.NAME
                )
            elif isinstance(rule_, Path):
                logger.warning(f'Loading rules from path "{rule_}"')
                if rule_.is_file():
                    if rule_.suffix != ".py":
                        logger.error(f'The path "{rule_}" must endswith ".py"')
                        return

                    rule_module_name = None
                    for path in self._module_path_finder.path:
                        try:
                            if rule_.stem == "__init__":
                                if rule_.resolve().parent.parent.samefile(Path(path)):
                                    rule_module_name = rule_.resolve().parent.name
                                    break
                            elif rule_.resolve().parent.samefile(Path(path)):
                                rule_module_name = rule_.stem
                                break
                        except OSError:
                            continue
                    if rule_module_name is None:
                        rel_path = rule_.resolve().relative_to(Path(".").resolve())
                        if rel_path.stem == "__init__":
                            rule_module_name = ".".join(rel_path.parts[:-1])
                        else:
                            rule_module_name = ".".join(
                                rel_path.parts[:-1] + (rel_path.stem,)
                            )

                    self._load_rules_from_module_name(
                        rule_module_name, rule_load_type or RuleLoadType.FILE
                    )
                else:
                    logger.error(f'The rule path "{rule_}" must be a file')
            else:
                logger.error(f"Type error: {rule_} can not be loaded as plugin")

    def load_rules(self, *rules: Union[Type[Rule], str, Path]):
        """加载规则。

        Args:
            *rules: 规则类、规则包x模块名称或者规则包模块文件路径。类型可以是 `Type[Rule]`, `str` 或 `pathlib.Path`。
                如果为 `Type[Rule]` 类型时，将作为规则类进行加载。
                如果为 `str` 类型时，将作为规则包模块名称进行加载，格式和 Python `import` 语句相同。
                    例如：`path.of.rule`。
                如果为 `pathlib.Path` 类型时，将作为规则包模块文件路径进行加载。
                    例如：`pathlib.Path("path/of/rule")`。
        """
        # self._extend_rules.extend(rules)
        return self._load_rules(*rules)
    
    def _load_rules_from_dirs(self, *dirs: Path):
        """从目录中加载规则包，以 `_` 开头的模块中的规则不会被导入。路径可以是相对路径或绝对路径。

        Args:
            *dirs: 储存包含规则的模块的模块路径。
                例如：`pathlib.Path("path/of/rules/")` 。
        """
        logger.info("Loading rules from dirs...")
        dirs = list(map(lambda x: str(x.resolve()), dirs))  # type: ignore  maybe remove?
        logger.warning(f'Loading rules from dirs "{", ".join(map(str, dirs))}"')
        self._module_path_finder.path.extend(dirs)  # type: ignore
        # type: ignore
        for rule_class, module in get_classes_from_dir(dirs, Rule):  # type: ignore
            self._load_rule_class(rule_class, RuleLoadType.DIR, module.__file__)
    
    def load_rules_from_dirs(self, *dirs: Path):
        """从目录中加载规则，以 `_` 开头的模块中的规则不会被导入。路径可以是相对路径或绝对路径。

        Args:
            *dirs: 储存包含rule的模块的模块路径。
                例如：`pathlib.Path("path/of/rules/")` 。
        """
        # self._extend_rule_dirs.extend(dirs)
        self._load_rules_from_dirs(*dirs)
        
    @property
    def rules(self) -> List[Type[Plugin]]:
        """当前已经加载的规则包的列表。"""
        return list(chain(*self.rules_priority_dict.values()))
    
    def __post_init__(self):
        if not self.bot.global_state.get('init', False):
            self.bot.global_state = dict()
            self.bot.global_state['init'] = True

            self._load_rules_from_dirs(Path(os.path.join("\\".join(os.path.dirname(__file__).split('\\')[:-2]),"rules"))) #*self.config.rule['rule_dirs'])
            # self._load_rules(*self.config.rule.rules)
            
        ...
    
    async def handle(self) -> None:
        """
        @TODO: HydroRollCore should be able to handle all signals and tokens from Psi.
        @BODY: HydroRollCore actives the rule-packages.
        """

        if self.event.message.get_plain_text() == '.core':
            await self.event.reply("HydroRollCore is running.")
        elif self.event.message.startswith('.show'):
            try:
                await self.event.reply(eval(self.event.message.get_plain_text()[6:]))
            except Exception as e:
                await self.event.reply(f"{e!r}")
                
    async def rule(self) -> bool:
        """
        @TODO: Psi should be able to handle all message first. 
        @BODY: lexer module will return a list of tokens, parser module will parse the tokens into a tree, and executor module will execute the tokens with a stack with a bool return value.
        """
        
        if self.event.type != "message":
            return False
        return self.event.message.get_plain_text().startswith(".")