from iamai import Plugin
from iamai.log import logger as log
import asyncio
import aiohttp

payload = None    

class Webhook(Plugin):
    async def handle(self) -> None:
        global payload
        if payload:
            log.info(payload[:5])
            await self.bot.get_adapter("cqhttp").call_api(
                "send_group_msg",
                group_id=126211793,
                message=payload
            )

    async def rule(self) -> bool:
        global payload
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get('http://localhost:3000') as response:
                    try:
                        payload = await response.text()
                        log.info(payload)
                        return True
                    except Exception as e:
                        log.info(f'Failed to fetch payload: {e}')
                        return False
            except Exception as e:
                return False