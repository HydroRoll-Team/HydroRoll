from iamai import Plugin
from numpy.random import Generator



class Exec(Plugin):

    priority = 1

    async def handle(self) -> None:
        try:
            content = [
                {
                    "type": "node",
                    "data": {
                        "name": f"{self.event.sender.nickname}",
                        "uin": f"{self.event.sender.user_id}",
                        "content": [
                            {
                                "type": "text",
                                "data": {
                                    "text": f"{eval(self.event.message.get_plain_text()[6:])}"
                                }
                            }
                        ]
                    }
                }
            ]
            res = await self.event.adapter.send_group_forward_msg(group_id=int(self.event.group_id), messages=content)
        except Exception as e:
            # await self.event.reply(f"ERROR！{e!r}")
            await self.event.reply(f"{eval(self.event.message.get_plain_text()[6:])}")

    async def rule(self) -> bool:
        return (
            self.event.type == "message"
            and
            self.event.message.get_plain_text().startswith(".show")
        )