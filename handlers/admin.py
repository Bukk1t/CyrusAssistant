from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.database import get_user_count


router = Router()


@router.message(Command("stats"))
async def stats(message: Message):
    users = get_user_count()

    await message.answer(
        "📊 Cyrus Statistics\n\n"
        f"👥 Users: {users}\n"
        "🤖 Status: Online"
    )