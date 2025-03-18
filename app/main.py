import asyncio
import os

from bot import bot, dp
from bot_utils import set_commands
from bot_router import bot_router

async def start_bot():
    os.mkdirs("./tmp", exist_ok=True)
    dp.include_router(bot_router)
    
    await bot.delete_webhook(drop_pending_updates=True)

    await set_commands()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())

