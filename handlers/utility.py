from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from datetime import datetime
from utils.uptime import get_uptime
from database.database import get_user_count

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