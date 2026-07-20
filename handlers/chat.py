from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def unknown_message(message: Message):
    await message.answer(
        "❓ I don't understand that command.\n\n"
        "Use /help to see what I can do."
    )