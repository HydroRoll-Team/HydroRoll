from typing import Set

from plugins.plugin_base import CommandPluginConfig


class Config(CommandPluginConfig):
    __config_name__ = "plugin_system_info"
    command: Set[str] = {"system"}
    """命令文本。"""
    message_str: str = "{message}"
    """最终发送消息的格式。"""
