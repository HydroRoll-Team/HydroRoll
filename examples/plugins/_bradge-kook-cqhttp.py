from iamai import Plugin


class Bradge(Plugin):
    async def handle(self) -> None:
        if self.event.adapter.name == "kook":
            await self.bot.get_adapter("cqhttp").call_api(
                "send_group_msg", 
                group_id=971050440,
                message=f"[{self.event.adapter.name} - {self.event.extra.author.username}]\n{self.event.message}"
                )
        elif self.event.adapter.name == "cqhttp":
            if self.event.group_id == 971050440:
                await self.bot.get_adapter("kook").call_api(
                    api="message/create", 
                    target_id=1661426334688259,
                    content=f"[{self.event.adapter.name} - {self.event.sender.nickname}]\n{self.event.message}"
                    )

    async def rule(self) -> bool:
        if self.event.adapter.name not in ["cqhttp","kook"]:
            return False
        if self.event.type not in ["message","9",9]:
            return False
        return True