# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import asyncio
import logging

# Ensure a single active event loop exists before Motor (database.py) and
# Pyrofork initialize so both bind to the same loop on Python 3.11+.
_loop = asyncio.new_event_loop()
asyncio.set_event_loop(_loop)

from config import Config
from pyrogram import Client as VJ, idle
from plugins.regix import restart_forwards

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

if __name__ == "__main__":
    VJBot = VJ(
        Config.BOT_SESSION,
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        in_memory=True,
        plugins=dict(root="plugins"),
    )

    async def _run_restart_forwards():
        try:
            await restart_forwards(VJBot)
        except Exception:
            logger.exception("Failed while restarting pending forwards")

    async def main():
        await VJBot.start()
        try:
            bot_info = await VJBot.get_me()
            logger.info("Bot Started as @%s", bot_info.username)
            print("Bot Started.", flush=True)
            asyncio.create_task(_run_restart_forwards())
            await idle()
        finally:
            await VJBot.stop()

    try:
        _loop.run_until_complete(main())
    finally:
        _loop.close()

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
