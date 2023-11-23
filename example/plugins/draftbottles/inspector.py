from iamai import Event, Depends, Bot
from .database import Database
from .permission import Permission
from .workroutes import WorkRoutes
from iamai.exceptions import GetEventTimeout
from iamai.adapter.onebot11.message import CQHTTPMessageSegment as ms


class Inspector:
    event: Event = Depends()
    bot: Bot = Depends()
    database: Database = Depends()
    permission: Permission = Depends()
    workroutes: WorkRoutes = Depends()

    async def test(self, *args):
        suffix = list(args)[0]
        try:
            return f"{eval(suffix)}"
        except Exception as e:
            return f"{e!r}"

    async def throw(self, *args):
        suffix = list(args)[0]
        config = list(args)[1]
        if len(suffix) == 0:
            """没有内容，则进入输入流"""
            try:
                content_event = await self.event.ask(
                    "在漂流瓶中要写下什么呢？（输入“取消”来取消扔漂流瓶操作。）", timeout=10
                )  # type: ignore
            except GetEventTimeout:
                return "超时。"
            except Exception as e:
                return f"{e!r}"
            else:
                if content_event.message.get_plain_text().lower() in ["取消", "cancel"]:
                    return ms.reply(content_event.message_id) + ms.text("已取消扔漂流瓶操作。")
                """有内容，进行审核"""
                content = content_event.message.get_plain_text()
                self._throw(content=content, event=content_event)
        else:
            """有内容，进行审核"""
            self._throw(content=suffix, event=self.event)

    async def get(self, *args):
        suffix = list(args)[0]
        try:
            return f"{eval(suffix)}"
        except Exception as e:
            return f"{e!r}"

    async def report(self, *args):
        suffix = list(args)[0]
        try:
            return f"{eval(suffix)}"
        except Exception as e:
            return f"{e!r}"

    async def comment(self, *args):
        suffix = list(args)[0]
        try:
            return f"{eval(suffix)}"
        except Exception as e:
            return f"{e!r}"

    async def check(self, *args):
        suffix = list(args)[0]
        try:
            return f"{eval(suffix)}"
        except Exception as e:
            return f"{e!r}"

    async def remove(self, *args):
        suffix = list(args)[0]
        try:
            return f"{eval(suffix)}"
        except Exception as e:
            return f"{e!r}"

    async def listb(self, *args):
        suffix = list(args)[0]
        try:
            return f"{eval(suffix)}"
        except Exception as e:
            return f"{e!r}"

    async def like(self, *args):
        suffix = list(args)[0]
        try:
            return f"{eval(suffix)}"
        except Exception as e:
            return f"{e!r}"

    async def resume(self, *args):
        suffix = list(args)[0]
        try:
            return f"{eval(suffix)}"
        except Exception as e:
            return f"{e!r}"

    async def clear(self, *args):
        suffix = list(args)[0]
        try:
            return f"{eval(suffix)}"
        except Exception as e:
            return f"{e!r}"

    async def delete(self, *args):
        suffix = list(args)[0]
        try:
            return f"{eval(suffix)}"
        except Exception as e:
            return f"{e!r}"

    async def details(self, *args):
        suffix = list(args)[0]
        try:
            return f"{eval(suffix)}"
        except Exception as e:
            return f"{e!r}"

    @staticmethod
    def _throw(content: str, **kwargs):
        """扔出漂流瓶"""
        event = kwargs.pop('event', None)
