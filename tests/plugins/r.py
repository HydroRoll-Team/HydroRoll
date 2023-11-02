from iamai import Plugin


class Roll(Plugin):
    async def handle(self) -> None:
        await self.event.reply("""Attack: 25
Damage: 9""")

    async def rule(self) -> bool:
        return self.event.type == "message" and self.event.message.startswith("/r")
