from aiogram import Router
from aiogram.types import Message

from database.database import add_message


router = Router()


@router.message()
async def chat_handler(message: Message):
    add_message(message.from_user.id)

    await message.answer(
        "❓ I don't understand that yet.\n\n"
        "Use /help to see available commands."
    )