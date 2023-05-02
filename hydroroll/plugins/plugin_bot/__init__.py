import re
from importlib.metadata import version
from plugins.plugin_base import CommandPluginBase
from hydroroll.config import GlobalConfig

from .config import Config


class HydroBot(CommandPluginBase[None, Config]):
    Config = Config
    CurrentConfig = GlobalConfig
    priority = 0

    def __post_init__(self):
        self.re_pattern = re.compile(r"(?P<bot_info_str>.*)", flags=re.I)

    def bot_info(self):
        info_str = f'{self.CurrentConfig._name} '\
                   f'{self.CurrentConfig._version}({self.CurrentConfig._svn}) '\
                   f'by {self.CurrentConfig._author} '\
                   f'on Python {self.CurrentConfig._python_ver_raw} '\
                   f'with {" & ".join([adapter + "("+version("iamai-adapter-"+adapter) +")" for adapter in dict(self.bot.config.adapter)])} '\
                   f'for iamai({self.CurrentConfig._iamai_version})'

        return info_str

    async def handle(self) -> None:
        await self.event.reply(
            self.format_str(self.config.message_str, self.bot_info())
        )
