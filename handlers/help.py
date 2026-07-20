from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "📚 Cyrus Assistant Commands:\n\n"

        "🚀 Basic:\n"
        "/start - Start the bot\n"
        "/help - Show this menu\n"
        "/about - About Cyrus\n\n"

        "🛠️ Utility:\n"
        "/ping - Check bot status\n"
        "/id - Show your Telegram ID\n"
        "/userinfo - Show your profile info\n"
        "/time - Show current time"

        "👑 Admin:
        "/stats - Show bot statistics"
    )