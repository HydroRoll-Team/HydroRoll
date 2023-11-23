from typing import Union
from iamai import Plugin, Event, Depends
from iamai.log import logger
from .config import Config
from iamai.event import MessageEvent
from .database import Database
from .permission import Permission
from .workroutes import WorkRoutes
from .inspector import Inspector


class Bottles(Plugin, config=Config):
    database: Database = Depends()
    permission: Permission = Depends()
    workroutes: WorkRoutes = Depends()
    inspector: Inspector = Depends()

    def __init__(self):
        self.text = None
        self.prefix = None
        self.suffix = None

    async def handle(self) -> None:
        self.namespace = next(
            (
                key
                for key, value in self.config.command_list.items()
                if value == self.prefix
            ),
            "",
        )
        logger.debug(
            f"Prefix: {self.prefix}, suffix: {self.suffix}, namespace: {self.namespace}"
        )
        if method := getattr(self.inspector, self.namespace, None):
            result = await method(self.suffix, self.config)
            if result:
                await self.event.reply(result)

    async def rule(self) -> bool:
        if not isinstance(self.event, MessageEvent):
            return False
        self.text = self.event.get_plain_text()
        for prefix in list(self.config.command_list.values()):
            if self.text.startswith(prefix):
                self.prefix = prefix
                self.suffix = self.text[len(self.prefix) + 1 :]
                return True
        return False
