import re
import sys
import platform
from importlib.metadata import version
from plugins.iamai_plugin_base import CommandPluginBase

from .config import Config


class BotInfo(CommandPluginBase[None, Config]):
    Config = Config

    def __post_init__(self):
        self.re_pattern = re.compile(r"(?P<bot_info_str>.*)", flags=re.I)

    async def handle(self) -> None:
        await self.event.reply(
            self.format_str(self.config.message_str,
                            f"{self.bot.config.Chien['self']['header']} HydroRoll!{self.bot.config.Chien['version']}({self.bot.config.Chien['svn']}) by {self.bot.config.Chien['author']} on Python {'.'.join(map(str, platform.python_version_tuple()[:3]))} with {' & '.join([adapter + '('+version('iamai-adapter-'+adapter)+')' for adapter in dict(self.bot.config.adapter)])} for iamai({version('iamai')})\n{self.bot.config.Chien['self']['info']}")
        )
