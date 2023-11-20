from iamai import Plugin
from numpy.random import Generator
from iamai.adapter.onebot11.message import CQHTTPMessage, CQHTTPMessageSegment
from iamai.log import logger

ms = CQHTTPMessageSegment


class R(Plugin):
    priority = 1

    async def handle(self) -> None:
        try:
            await self.event.reply("test")
        except Exception as e:
            # await self.event.reply(f"ERROR！{e!r}")
            logger.info("ERROR with message: {}".format(e))

    async def rule(self) -> bool:
        return (
            self.event.type == "message"
            and self.event.message.get_plain_text().startswith(".show")
        )
