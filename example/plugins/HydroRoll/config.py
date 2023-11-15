from randomgen import AESCounter
from numpy.random import Generator
import argparse
import sys
from os.path import dirname, dirname, join, abspath
import platform
from importlib.metadata import version
import os
from typing import Set, Optional
from iamai import ConfigModel
import datetime

from typing import Set

from pydantic import Field


class BasePluginConfig(ConfigModel):
    message_str: str = "{message}"
    """最终发送消息的格式。"""


class RegexPluginConfig(BasePluginConfig):
    pass


class CommandPluginConfig(RegexPluginConfig):
    __config_name__ = "HydroRoll"
    command_prefix: Set[str] = Field(default_factory=lambda: {".", "。"})
    """命令前缀。"""
    command: Set[str] = Field(default_factory=set)
    """命令文本。"""
    ignore_case: bool = True
    """忽略大小写。"""


class Color:
    # 定义ANSI转义序列
    RESET = "\033[0m"
    BLUE_BASE = "\033[36m"
    BLUE_DARK = "\033[34m"
    BLUE_DARKER = "\033[32m"
    BLUE_DARKEST = "\033[30m"


# 定义全局配置类
class GlobalConfig:
    _name = "HydroRoll[水系]"
    _version = "0.1.0"
    _svn = "2"
    _author = "简律纯"
    _iamai_version = version("iamai")
    _python_ver = sys.version
    _python_ver_raw = ".".join(map(str, platform.python_version_tuple()[:3]))
    _base_dir = dirname(abspath("__file__"))
    _hydro_dir = dirname(abspath(__file__))
    _copyright = f"""\033[36m
                  _             __       _ _ 
  /\  /\_   _  __| |_ __ ___   /__\ ___ | | |
 / /_/ / | | |/ _` | '__/ _ \ / \/// _ \| | |
/ __  /| |_| | (_| | | | (_) / _  \ (_) | | |
\/ /_/  \__, |\__,_|_|  \___/\/ \_/\___/|_|_|
        |___/                                

\033[4m{_name} [版本 {_version}]\033[0m\033[36m
(c) HydroRoll-Team contributors, {_author}。
Github: https://github.com/HydroRoll-Team
Under the MIT License, see LICENSE for more details.
"""


class Directory(object):
    def __init__(self, _path: str) -> None:
        self.current_path = _path

    def get_dice_dir_list(self, _prefix: str) -> list:
        return [
            os.path.join(self.current_path, f"{_prefix}", *dirs)
            for dirs in [
                ["config"],
                ["data"],
                ["rules"],
                ["scripts"],
                ["web", "frontend"],
                ["web", "backend"],
            ]
        ]


class FileManager(object):
    def __init__(self, _path: str) -> None:
        self.current_path = _path

    def get_file_list(self, _dir: str):
        return {
            "web;frontend": "index.html",
            "data": "censor.json",
        }


class Models:
    """模型管理类"""

    def __init__(self) -> None:
        self.builtin_models = {"hola": "hola.pkl"}

    def get_models_dict(self) -> dict:
        return self.builtin_models
