from iamai import Plugin
from numpy.random import Generator
from iamai.adapter.onebot11.message import CQHTTPMessage, CQHTTPMessageSegment
from iamai.log import logger
from lupa import LuaRuntime
from iamai.utils import sync_func_wrapper
import asyncio

lua = LuaRuntime(unpack_returned_tuples=True)
ms = CQHTTPMessageSegment


class Lua(Plugin):
    priority = 1
    prefix = "/lua"

    async def handle(self) -> None:
        try:
            self.suffix = self.event.message.get_plain_text()[len(self.prefix) + 1 :]



            class msg:
                priority = self.priority
                prefix = self.prefix
                fromMsg = self.event.message
                suffix = self.suffix
                event = self.event

                def echo(self, message=None):
                    if not message:
                        return self.__str__

                    loop = asyncio.get_event_loop()
                    coro = self.event.reply(message)
                    asyncio.run_coroutine_threadsafe(coro, loop)

                def ask(self, message=None, timeout=10):
                    if not message:
                        return self.__str__

                    loop = asyncio.get_event_loop()
                    coro = self.event.ask(message, timeout=timeout)
                    asyncio.run_coroutine_threadsafe(coro, loop)


            lua.globals().msg = msg
            lua.globals().event = self.event
            # logger.info(lua.eval(self.suffix))
            if result := lua.eval(self.suffix):
                await self.event.reply(result)
        except Exception as e:
            await self.event.reply(f"ERROR！{e!r}")
            logger.info("ERROR with message: {}".format(e))

    async def rule(self) -> bool:
        return (
            self.event.type == "message"
            and self.event.message.get_plain_text().startswith(self.prefix)
        )
