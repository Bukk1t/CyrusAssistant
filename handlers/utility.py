from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from datetime import datetime
from utils.uptime import get_uptime
from database.database import get_user_count
from services.user_service import get_profile

router = Router()


@router.message(Command("ping"))
async def ping(message: Message):
    await message.answer("🏓 Pong!")


@router.message(Command("id"))
async def user_id(message: Message):
    await message.answer(
        f"🆔 Your Telegram ID:\n{message.from_user.id}"
    )


@router.message(Command("userinfo"))
async def user_info(message: Message):
    user = message.from_user

    await message.answer(
        "👤 User Info\n\n"
        f"Name: {user.full_name}\n"
        f"Username: @{user.username}\n"
        f"ID: {user.id}"
    )


@router.message(Command("time"))
async def current_time(message: Message):
    now = datetime.now()

    await message.answer(
        f"🕒 Current time:\n{now.strftime('%Y-%m-%d %H:%M:%S')}"
    )

@router.message(Command("status"))
async def status(message: Message):
    users = get_user_count()

    await message.answer(
        "🤖 Cyrus Status\n\n"
        "🟢 Online\n"
        f"⏱ Uptime: {get_uptime()}\n"
        f"👥 Users: {users}"
    )
    
@router.message(Command("profile"))
async def profile(message: Message):
    user = get_profile(message.from_user.id)

    if user is None:
        await message.answer(
            "❌ No profile found.\n\n"
            "Use /start first."
        )
        return

    user_id, username, first_name, joined_at, messages, last_seen = user

    username_text = f"@{username}" if username else "No username"

    await message.answer(
        "👤 Cyrus Profile\n\n"
        f"🆔 ID: {user_id}\n"
        f"👋 Name: {first_name}\n"
        f"🏷 Username: {username_text}\n"
        f"💬 Messages: {messages}\n"
        f"🕒 Last Seen: {last_seen}"
        f"📅 Joined: {joined_at}\n"
    )