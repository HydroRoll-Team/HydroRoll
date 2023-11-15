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
from .command import Set, Get
from iamai.exceptions import GetEventTimeout
from iamai.event import MessageEvent

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
        global flag

        args = self.event.get_plain_text().split(" ")
        command_list = [".root", ".roots", ".core", ".set", ".get", ".test"]
        current_cmd = args[0]
        flag = True in [cmd.startswith(current_cmd) for cmd in command_list]
        logger.info(f"Command {current_cmd} not found with flag {flag}")
        if args[0] in [".root", ".roots"]:
            import requests
            data = requests.get("https://vercel-hitokoto.vercel.app/api/roots").json()
            await self.event.reply(data["line"])
        else:
            if args[0] == ".core":
                ...
            # if args[0].startswith(".set"):
            #     resolve = Set(args[1:])  # TODO: handle multiple sets
            # elif args[0].startswith(".get"):
            #     resolve = Get(args[1:])  # TODO: handle multiple gets
            elif args[0].startswith(".test"):
                try:
                    result = eval(self.event.message.get_plain_text()[5:])
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
        return isinstance(self.event, MessageEvent)

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

    # async def ask(self, ask_text: str | None, timeout: int = 10) -> None:
    #     if ask_text:
    #         await self.event.reply(ask_text)
    #     try:
    #         event = await self.event.adapter.get(
    #             lambda x: x.type == "message"
    #             and x.group_id == self.event.group_id
    #             and x.user_id == self.event.user_id,
    #             timeout=timeout,
    #         )
    #         return event
    #     except GetEventTimeout as e:
    #         raise GetEventTimeout from e
