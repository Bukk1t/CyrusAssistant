import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramNetworkError

from config import BOT_TOKEN
from database.database import initialize_database

from handlers.start import router as start_router
from handlers.help import router as help_router
from handlers.about import router as about_router
from handlers.buttons import router as buttons_router
from handlers.chat import router as chat_router
from handlers.utility import router as utility_router
from handlers.tools import router as tools_router
from handlers.fun import router as fun_router
from handlers.admin import router as admin_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN was not found. Check your .env file.")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Register routers
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
        print("Starting Cyrus...")
        await dp.start_polling(bot)

    except TelegramNetworkError:
        print(
            "\n❌ Cannot connect to Telegram API.\n"
            "Check your internet/VPN/network filtering.\n"
        )

    finally:
        await bot.session.close()
        print("Bot stopped.")


if __name__ == "__main__":
    asyncio.run(main())