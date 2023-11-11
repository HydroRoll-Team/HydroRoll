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
# 创建全局 ArgumentParser 对象
global_parser = argparse.ArgumentParser(description="HydroRoll[水系] 全局命令参数")


class Color:
    # 定义ANSI转义序列
    RESET = '\033[0m'
    BLUE_BASE = '\033[36m'
    BLUE_DARK = '\033[34m'
    BLUE_DARKER = '\033[32m'
    BLUE_DARKEST = '\033[30m'


class BasePluginConfig(ConfigModel):
    __config_name__ = ""
    handle_all_message: bool = True
    """是否处理所有类型的消息，此配置为 True 时会覆盖 handle_friend_message 和 handle_group_message。"""
    handle_friend_message: bool = True
    """是否处理好友消息。"""
    handle_group_message: bool = True
    """是否处理群消息。"""
    accept_group: Optional[Set[int]] = None
    """处理消息的群号，仅当 handle_group_message 为 True 时生效，留空表示处理所有群。"""
    message_str: str = "*{user_name} {message}"
    """最终发送消息的格式。"""


class RegexPluginConfig(BasePluginConfig):
    pass


class CommandPluginConfig(RegexPluginConfig):
    command_prefix: Set[str] = {":"}
    """命令前缀。"""
    command: Set[str] = {}
    """命令文本。"""
    ignore_case: bool = True
    """忽略大小写。"""


# 定义全局配置类
class GlobalConfig(CommandPluginConfig):
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
    _rg = Generator(AESCounter())
    SEED = _rg.random()  # 随机数种子

    # 定义系统组件

    class HydroSystem:
        def __init__(self):
            self.parser = argparse.ArgumentParser(
                description="HydroRoll[水系].system 系统命令参数"
            )
            self.subparsers = self.parser.add_subparsers()
            self.status_parser = self.subparsers.add_parser(
                "status", aliases=["stat", "state"], help="系统状态"
            )
            self.reload_parser = self.subparsers.add_parser(
                "reload", aliases=["rld"], help="重新加载系统"
            )
            self.restart_parser = self.subparsers.add_parser(
                "restart", aliases=["rst"], help="重启系统"
            )
            self.collect_parser = self.subparsers.add_parser(
                "collect", aliases=["gc"], help="释放 python 内存"
            )
            self.help = "\n".join(
                self.parser.format_help()
                .replace("\r\n", "\n")
                .replace("\r", "")
                .split("\n")[2:-3]
            )

    class HydroBot:
        def __init__(self) -> None:
            self.parser = argparse.ArgumentParser(description="Bot命令")


class Directory(object):
    def __init__(self, _path: str) -> None:
        self.current_path = _path

    def get_dice_dir_list(self, _prefix: str) -> list:

        return [
            os.path.join(self.current_path, f'{_prefix}', *dirs)
            for dirs in [
                ['config'],
                ['data'],
                ['rules'],
                ['scripts'],
                ['web', 'frontend'],
                ['web', 'backend'],
            ]
        ]


class FileManager(object):
    def __init__(self, _path: str) -> None:
        self.current_path = _path

    def get_file_list(self, _dir: str):
        return {
            'web;frontend': 'index.html',
            'data': 'censor.json',
        }


class Models:
    """模型管理类"""

    def __init__(self) -> None:
        self.builtin_models = {'hola': 'hola.pkl'}

    def get_models_dict(self) -> dict:
        return self.builtin_models

