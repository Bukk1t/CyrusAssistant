from aiogram import Router
from aiogram.types import Message

from services.user_service import register_message


router = Router()


@router.message()
async def chat_handler(message: Message):

    await message.answer(
        "❓ I don't understand that yet.\n\n"
        "Use /help to see available commands."
    )