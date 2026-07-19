from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "📚 Cyrus Assistant Commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show this menu\n"
        "/about - About Cyrus"
    )