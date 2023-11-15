import difflib
import re
import time
import random
from abc import ABC, abstractmethod
from typing import Type, Union, Generic, TypeVar
from iamai import Plugin

import re
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from iamai import MessageEvent, Plugin
from iamai.typing import StateT

from .config import BasePluginConfig, CommandPluginConfig, RegexPluginConfig

ConfigT = TypeVar("ConfigT", bound=BasePluginConfig)
RegexPluginConfigT = TypeVar("RegexPluginConfigT", bound=RegexPluginConfig)
CommandPluginConfigT = TypeVar("CommandPluginConfigT", bound=CommandPluginConfig)


class BasePlugin(
    Plugin[MessageEvent[Any], StateT, ConfigT],
    ABC,
    Generic[StateT, ConfigT],
):
    def format_str(self, format_str: str, message_str: str = "") -> str:
        return format_str.format(
            message=message_str,
            user_name=self.get_event_sender_name(),
            user_id=self.get_event_sender_id(),
        )

    def get_event_sender_name(self) -> str:
        from iamai.adapter.onebot11.event import MessageEvent as OneBotMessageEvent

        if isinstance(self.event, OneBotMessageEvent):
            return self.event.sender.nickname or ""
        return ""

    def get_event_sender_id(self) -> str:
        from iamai.adapter.onebot11.event import MessageEvent as OneBotMessageEvent

        if isinstance(self.event, OneBotMessageEvent):
            if self.event.sender.user_id is not None:
                return str(self.event.sender.user_id)
            return ""
        return ""

    async def rule(self) -> bool:
        return isinstance(self.event, MessageEvent) and self.str_match(
            self.event.get_plain_text()
        )

    @abstractmethod
    def str_match(self, msg_str: str) -> bool:
        raise NotImplementedError


class RegexPluginBase(BasePlugin[StateT, RegexPluginConfigT], ABC):
    msg_match: re.Match[str]
    re_pattern: re.Pattern[str]

    def str_match(self, msg_str: str) -> bool:
        msg_str = msg_str.strip()
        msg_match = self.re_pattern.fullmatch(msg_str)
        if msg_match is None:
            return False
        self.msg_match = msg_match
        return bool(self.msg_match)


class CommandPluginBase(RegexPluginBase[StateT, CommandPluginConfigT], ABC):
    command_match: re.Match[str]
    command_re_pattern: re.Pattern[str]

    def str_match(self, msg_str: str) -> bool:
        if not hasattr(self, "re_pattern"):
            self.re_pattern = re.compile(
                f'[{"".join(self.config.command_prefix)}]'
                f'({"|".join(self.config.command)})'
                r"\s*(?P<command_args>.*)",
                flags=re.I if self.config.ignore_case else 0,
            )
        msg_str = msg_str.strip()
        msg_match = self.re_pattern.fullmatch(msg_str)
        if not msg_match:
            return False
        self.msg_match = msg_match
        command_match = self.re_pattern.fullmatch(self.msg_match.group("command_args"))
        if not command_match:
            return False
        self.command_match = command_match
        return True


class PseudoRandomGenerator:
    """线性同余法随机数生成器"""

    def __init__(self, seed):
        self.seed = seed

    def generate(self):
        while True:
            self.seed = (self.seed * 1103515245 + 12345) % (2**31)
            yield self.seed


class HydroDice:
    """水系掷骰组件

    一些 API 相关的工具函数

    """

    def __init__(self, seed):
        self.generator = PseudoRandomGenerator(seed)

    def roll_dice(
        self,
        _counts: int | str,
        _sides: int | str,
        is_reversed: bool = False,
        streamline: bool = False,
        threshold: int | str = 5,
    ) -> str:
        """普通掷骰
        Args:
            _counts (int | str): 掷骰个数.
            _sides (int | str): 每个骰子的面数.
            is_reversed (bool, optional): 倒序输出. Defaults to False.
            streamline (bool, optional): 忽略过程. Defaults to False.
            threshold (int | str, optional): streamline 的阈值. Defaults to 5.

        Returns:
            str: 表达式结果.
        """
        rolls = []
        for _ in range(int(_counts)):
            roll = next(self.generator.generate()) % _sides + 1
            rolls.append(roll)
        total = sum(rolls)

        if streamline:
            return str(total)
        if len(rolls) > int(threshold):
            return str(total)
        rolls_str = " + ".join(str(r) for r in rolls)
        return f"{total} = {rolls_str}" if is_reversed else f"{rolls_str} = {total}"


def find_max_similarity(input_string, string_list):
    """寻找最大的相似度"""
    max_similarity = 0
    max_string = ""

    for string in string_list:
        similarity = difflib.SequenceMatcher(None, input_string, string).quick_ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            max_string = string

    return max_string, max_similarity


def check_file(filename: str) -> bool:
    """根据给定参数校验文件夹内文件完整性"""

    return False
