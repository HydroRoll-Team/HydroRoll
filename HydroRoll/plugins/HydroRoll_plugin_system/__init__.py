import re
from plugins.HydroRoll_plugin_base import CommandPluginBase
from .config import Config
import psutil
import time
from HydroRoll.config import GlobalConfig


class System(CommandPluginBase[None, Config]):
    priority: int = 0
    Config = Config
    CurrentConfig = GlobalConfig

    def __post_init__(self):
        self.re_pattern = re.compile(r"(?P<system_info_str>.*)", flags=re.I)

    def eventReply(self, message: str):
        return self.event.reply(
            self.format_str(self.config.message_str, message)
        )

    def get_system_status(self) -> str:
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        current_time = time.time()
        start_time = psutil.Process().create_time()

        uptime_seconds = int(current_time - start_time)
        uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

        info_str = f"{self.CurrentConfig._name} Ver.{self.CurrentConfig._version}"
        info_str += f"({self.CurrentConfig._svn}) built in Python {self.CurrentConfig._python_ver}\n"
        info_str += f"本地时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n"
        info_str += f"已启动时间：{uptime_str}\n"
        info_str += f"CPU使用率：{cpu_usage}%\n"
        info_str += f"内存占用率：{memory_usage}%\n"
        info_str += f"磁盘使用率：{disk_usage}%"

        return info_str

    async def handle(self) -> None:
        system = self.CurrentConfig.HydroSystem()
        try:
            sub_command = self.event.get_plain_text().split()[1]
        except IndexError:
            sub_command = ""

        if sub_command in ["status", "s"]:
            await self.event.reply(
                self.format_str(self.config.message_str,
                                self.get_system_status())
            )
        elif sub_command in ["restart", "rst"]:
            await self.event.reply(
                self.format_str(self.config.message_str, "正在重启系统...")
            )
            self.bot.restart()

        elif sub_command in ["reload", "rld"]:
            await self.event.reply(
                self.format_str(self.config.message_str, "正在重载...")
            )
            self.bot.reload_plugins()
            await self.event.reply(
                self.format_str(self.config.message_str,
                                f"已加载{len(self.bot.plugins)}枚插件")
            )
        else:
            await self.event.reply(
                self.format_str(self.config.message_str, system.help)
            )
