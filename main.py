import asyncio
import logging

from database.database import initialize_database
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.help import router as help_router
from handlers.about import router as about_router
from handlers.buttons import router as buttons_router
from handlers.chat import router as chat_router

from handlers.utility import router as utility_router
from handlers.tools import router as tools_router
from handlers.fun import router as fun_router
from handlers.admin import router as admin_router

logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


dp.include_router(start_router)
dp.include_router(help_router)
dp.include_router(about_router)
dp.include_router(buttons_router)
dp.include_router(chat_router)

dp.include_router(utility_router)
dp.include_router(tools_router)
dp.include_router(fun_router)
dp.include_router(admin_router)

async def main():
    initialize_database()

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

        
if __name__ == "__main__":
    asyncio.run(main())