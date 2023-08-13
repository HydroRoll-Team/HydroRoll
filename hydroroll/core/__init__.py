from abc import ABC, abstractmethod
import os, os.path
from enum import Enum
from iamai.config import ConfigModel
from iamai.utils import is_config_class
from typing import Generic, NoReturn, Optional, Type, TYPE_CHECKING
from ...HydroRoll.typing import T_Event, T_Config

if TYPE_CHECKING:
    from iamai.bot import Bot
    
class RuleLoadType(Enum):
    """插件加载类型。"""

    DIR = "dir"
    NAME = "name"
    FILE = "file"
    CLASS = "class"
    

class Rule(ABC, Generic[T_Event, T_Config]):
    """所有 iamai 插件的基类。

    Attributes:
        event: 当前正在被此插件处理的事件。
        priority: 插件的优先级，数字越小表示优先级越高，默认为 0。
        block: 插件执行结束后是否阻止事件的传播。True 表示阻止。
        __rule_load_type__: 插件加载类型，由 iamai 自动设置，反映了此插件是如何被加载的。
        __rule_file_path__: 当插件加载类型为 `RuleLoadType.CLASS` 时为 `None`，
            否则为定义插件在的 Python 模块的位置。
    """

    event: T_Event
    priority: int = 0
    Config: Type[ConfigModel]

    __rule_load_type__: RuleLoadType
    __rule_file_path__: Optional[str]

    def __init__(self, event: T_Event):
        self.event = event

        if not hasattr(self, "priority"):
            self.priority = 0

        self.get = self.bot.get

        self.__post_init__()

    def __post_init__(self):
        """用于初始化后处理，被 `__init__()` 方法调用。"""
        pass

    @property
    def name(self) -> str:
        """规则类名称。"""
        return self.__class__.__name__

    @property
    def bot(self) -> "Bot":
        """机器人对象。"""
        return self.event.adapter.bot
    
    @property
    def config(self) -> Optional[T_Config]:
        """规则包配置。"""
        config_class: ConfigModel = getattr(self, "Rule", None)
        if is_config_class(config_class):
            return getattr(self.config.rule, config_class.__config_name__, None)
        return None