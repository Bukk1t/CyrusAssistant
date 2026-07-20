from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.main import main_keyboard
from database.database import add_user


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    user = message.from_user

    add_user(
        user_id=user.id,
        username=user.username,
        first_name=user.first_name,
    )

    await message.answer(
        "👋 Welcome to Ask Cyrus!\n\n"
        "The bot is online!",
        reply_markup=main_keyboard
    )