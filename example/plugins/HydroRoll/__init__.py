"""中间件"""
import re
import json
import joblib
import os
import shutil

from iamai import ConfigModel, Plugin
from iamai.log import logger
from iamai.exceptions import GetEventTimeout
from iamai.event import MessageEvent, Event
from iamai.typing import StateT

from .config import Directory, GlobalConfig, Models
from .utils import *
from .models.Transformer import query

from .config import (
    BasePluginConfig,
    CommandPluginConfig,
    RegexPluginConfig,
    GlobalConfig,
)

from ast import literal_eval
from os.path import dirname, join, abspath
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar
from typing_extensions import Annotated

ConfigT = TypeVar("ConfigT", bound=BasePluginConfig)
RegexPluginConfigT = TypeVar("RegexPluginConfigT", bound=RegexPluginConfig)
CommandPluginConfigT = TypeVar("CommandPluginConfigT", bound=CommandPluginConfig)


BASE_DIR = dirname(abspath("__file__"))
HYDRO_DIR = dirname(abspath(__file__))
APP_DIR = join(BASE_DIR, "HydroRoll")

# logger.info(GlobalConfig._copyright)


class Dice(Plugin[MessageEvent, Annotated[dict, {}], RegexPluginConfig]):
    """中间件"""

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
            try:
                import aiohttp

                async with aiohttp.ClientSession() as session:
                    async with session.get("https://api.hydroroll.team/api/roots") as response:
                        data = await response.json()
                        await self.event.reply(data["line"])
            except Exception as e:
                await self.event.reply(f"{e!r}")
        elif args[0] == ".core":
            await self.event.reply(f"{self.state}")
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
        """我想睡觉, 但我失眠了。"""
        self.models = self._load_models(self.model_path_list, self.model_dict)
 