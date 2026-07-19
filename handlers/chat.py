from aiogram import Router
from aiogram.types import Message

from services.ai import get_ai_response


router = Router()


@router.message()
async def chat_handler(message: Message):
    response = await get_ai_response(message.text)

    await message.answer(response)