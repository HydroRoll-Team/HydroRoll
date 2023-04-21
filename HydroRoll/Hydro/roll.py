from iamai import Plugin

class Roll(Plugin):
    async def handle(self) -> None:
        await self.event.reply("1")
        
    async def rule(self) -> bool:
        return(
            self.event.adapter.name == "cqhttp" and
            self.event.get_plain_text() == "1"
        )