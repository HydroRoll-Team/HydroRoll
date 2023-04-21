import re
import sys
from plugins.iamai_plugin_base import CommandPluginBase
from .config import Config
import psutil
import time


class SystemInfo(CommandPluginBase[None, Config]):
    priority: int = 0
    Config = Config

    def __post_init__(self):
        self.re_pattern = re.compile(r"(?P<bot_info_str>.*)", flags=re.I)

    def get_system_info(self) -> str:
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        current_time = time.time()
        start_time = psutil.Process().create_time()

        uptime_seconds = int(current_time - start_time)
        uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

        info_str = f"HydroRoll!{self.bot.config.Chien['version']}({self.bot.config.Chien['svn']}) built in Python {sys.version}\n"
        info_str += f"本地时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n"
        info_str += f"已启动时间：{uptime_str}\n"
        info_str += f"CPU使用率：{cpu_usage}%\n"
        info_str += f"内存占用率：{memory_usage}%\n"
        info_str += f"磁盘使用率：{disk_usage}%"

        return info_str

    async def handle(self) -> None:
        system_info = self.get_system_info()
        message_str = f"{system_info}"
        await self.event.reply(
            self.format_str(self.config.message_str,message_str)
        )