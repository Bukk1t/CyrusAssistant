import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.start import router as start_router
from handlers.help import router as help_router
from handlers.about import router as about_router
from handlers.buttons import router as buttons_router

logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


dp.include_router(start_router)
dp.include_router(help_router)
dp.include_router(about_router)
dp.include_router(buttons_router)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())