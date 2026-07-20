from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.main import main_keyboard
from services.user_service import register_user


router = Router()


@router.message(CommandStart())
async def start(message: Message):

    await message.answer(
        "👋 Welcome to Ask Cyrus!\n\n"
        "The bot is online!",
        reply_markup=main_keyboard
    )