from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def chat_handler(message: Message):
    await message.answer(
        "🤖 Cyrus received your message:\n\n"
        f"{message.text}"
    )