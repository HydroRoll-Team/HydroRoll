"""中间件"""
import json
import joblib
import os
import shutil
from ast import literal_eval
from os.path import dirname, join, abspath
from iamai import ConfigModel, Plugin
from iamai.log import logger
from .config import Directory, GlobalConfig, Models
from .utils import *
from .models.Transformer import query

BASE_DIR = dirname(abspath("__file__"))
HYDRO_DIR = dirname(abspath(__file__))
APP_DIR = join(BASE_DIR, "HydroRoll")

# logger.info(GlobalConfig._copyright)


class HydroRoll(Plugin):
    """中间件"""

    class Config(ConfigModel):
        __config_name__ = "HydroRoll"

    priority = 0

    # TODO: HydroRollCore should be able to handle all signals and tokens from Psi.
    logger.info("Loading HydroRollCore...")

    def __post_init__(self):
        self.state = {}
        self.model_path_list = []
        self.bot.global_state["HydroRoll"] = {}
        self.model_dict = Models().get_models_dict()

        self.model_path_list.append(join(BASE_DIR, "models"))
        self.model_path_list.append(join(HYDRO_DIR, "models"))
        self.model_path_list.append(join(BASE_DIR, "HydroRoll", "models"))

        self.load_models()

    async def handle(self) -> None:
        """
        @TODO: HydroRollCore should be able to handle all signals and tokens from Psi.
        @BODY: HydroRollCore actives the rule-packages.
        """

        if self.event.message.get_plain_text() == ".core":
            await self.event.reply("HydroRollCore is running.")
        if self.event.message.startswith(".set"):
            arg_list: list = self.event.message.get_plain_text().split()
            sub_cmd: str = arg_list[1]
            if sub_cmd == ("censor"):
                operator: str = arg_list[2]
                censor_list: list = arg_list[3:]
                pattern = re.compile(r"[+-](\d?=?)(.*)")

                try:
                    with open(
                        join(APP_DIR, "data", "censor.json"), "r+", encoding="utf8"
                    ) as f:
                        censor_content = json.load(f)
                except (FileNotFoundError, json.JSONDecodeError):
                    censor_content = {}

                censor_list = list(filter(lambda x: pattern.match(x), censor_list))

                with open(
                    join(APP_DIR, "data", "censor.json"), "w+", encoding="utf8"
                ) as f:
                    if operator in ["add", "+"]:
                        for item in censor_list:
                            match = pattern.match(item)
                            censor_content[match.group(2)] = int(
                                match.group(1).replace("=", "")
                            )
                    elif operator in ["remove", "rmv", "-"]:
                        for item in censor_list:
                            match = pattern.match(item)
                            keyword = match.group(2)
                            if keyword in censor_content:
                                del censor_content[keyword]
                    elif operator in ["list", "map"]:
                        pass  # do something else

                    json.dump(censor_content, f, ensure_ascii=False, indent=4)
        elif self.event.message.startswith(".get"):
            ...

        elif self.event.message.startswith(".test"):
            try:
                result = eval(self.event.message.get_plain_text()[5:]) #literal_eval(self.event.message.get_plain_text()[5:])
                await self.event.reply(str(result))
            except Exception as error:
                await self.event.reply(f"{error!r}")

    async def rule(self) -> bool:
        """
        @TODO: Psi should be able to handle all message first.
        @BODY: lexer module will return a list of tokens, parser module will parse the tokens into a tree, and executor module will execute the tokens with a stack with a bool return value.
        """
        logger.info("loading psi...")
        if (
            not self.bot.global_state["HydroRoll"].get("hola")
            and self.event.type == "message"
            and self.event.message_type == "private"
            and not os.path.exists(join(BASE_DIR, "HydroRoll"))
        ):
            # hola = self.models["hola"]
            # _, max_similarity = find_max_similarity(
            #     self.event.message.get_plain_text(), hola
            # )
            max_similarity = 1
            if max_similarity > 0.51:
                self.init_directory()
                self.bot.global_state["HydroRoll"]["hola"] = True
                await self.event.reply("验证成功√ 正在初始化水系目录...")
                logger.info(GlobalConfig._copyright)
        return self.event.adapter.name in ["cqhttp", "kook", "console", "mirai"]

    def _init_directory(self, _prefix: str = ""):
        """初始化水系目录"""
        for _ in Directory(BASE_DIR).get_dice_dir_list(_prefix):
            if not os.path.exists(_):
                os.makedirs(_)

    def _init_file(self, _prefix: str = ""):
        """初始化文件"""

    def init_directory(self, _prefix: str = "HydroRoll"):
        """在指定目录生成水系文件结构"""
        self._init_directory(_prefix=_prefix)

    def _load_model(self, path: str, model_file: str):
        if model_file is None:
            model_file = ""
        return joblib.load(join(path, f"{model_file}"))

    def _load_models(self, model_path_list: list, model_dict: dict) -> dict:
        """加载指定模型, 当然也可能是数据集"""
        models = {}
        for path in model_path_list:
            for model_name, model_file in model_dict.items():
                if os.path.exists(join(path, model_file)):
                    models[model_name] = self._load_model(path, model_file)
                    logger.success(f'Succeeded to load model "{model_name}"')
        return models

    def load_models(self):
        self.models = self._load_models(self.model_path_list, self.model_dict)


