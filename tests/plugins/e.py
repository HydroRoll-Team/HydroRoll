from iamai import Plugin

class Exec(Plugin):
    async def handle(self) -> None:
        try:
            await self.event.reply(eval(self.event.raw_message[5:]))
        except Exception as e:
            await self.event.reply(f"ERROR:\n\t{e}")
            
    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        try:
            return self.event.message.get_plain_text().startswith(".show")
        except:
            return False