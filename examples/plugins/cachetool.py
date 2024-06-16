from cachetools import cached
import time

from iamai import Plugin
from iamai.event import MessageEvent


class CachedPlugin(Plugin):
    async def handle(self) -> None:
        # without cached
        def fib(n):
            return n if n < 2 else fib(n - 1) + fib(n - 2)

        s = time.time()
        await self.event.reply(f"{fib(36)}")
        await self.event.reply(f"Time Taken: {time.time() - s}")

        # Now using cached
        s = time.time()

        # Use this decorator to enable caching
        @cached(cache={})
        def fib(n):
            return n if n < 2 else fib(n - 1) + fib(n - 2)

        await self.event.reply(f"{fib(36)}")
        await self.event.reply(f"Time Taken(cached): {time.time() - s}")

    async def rule(self) -> bool:
        return (
            isinstance(self.event, MessageEvent)
            and self.event.get_plain_text() == "/cachetools"
        )
