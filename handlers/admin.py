from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.database import get_user_count
from utils.admin import is_admin


router = Router()


@router.message(Command("stats"))
async def stats(message: Message):
    if not is_admin(message.from_user.id):
        await message.answer(
            "❌ You do not have permission to use this command."
        )
        return

    users = get_user_count()

    await message.answer(
        "📊 Cyrus Statistics\n\n"
        f"👥 Users: {users}\n"
        "🤖 Status: Online"
    )