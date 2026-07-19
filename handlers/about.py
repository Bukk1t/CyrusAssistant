from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("about"))
async def about_command(message: Message):
    await message.answer(
        "🤖 Ask Cyrus\n\n"
        "A personal AI assistant built with Python and Aiogram."
    )