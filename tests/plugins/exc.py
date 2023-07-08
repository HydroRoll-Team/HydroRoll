from iamai import Plugin
import os
class Exec(Plugin):
    async def handle(self) -> None:
        from hydroroll.config import ConfigManager, GlobalConfig
        tmpConf = ConfigManager(os.path.join(GlobalConfig._current_path, "config", "userConf.dat"))
        tmpConf.load()
        await self.event.reply(str(tmpConf.properties))
        
        
    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return self.event.message.startswith("t")

print(1)