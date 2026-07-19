from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: message.text == "📚 Help")
async def help_button(message: Message):
    await message.answer(
        "📚 Commands:\n\n"
        "/start\n"
        "/help\n"
        "/about"
    )


@router.message(lambda message: message.text == "ℹ️ About")
async def about_button(message: Message):
    await message.answer(
        "🤖 Ask Cyrus\n\n"
        "Your personal AI assistant."
    )


@router.message(lambda message: message.text == "🤖 Ask Cyrus")
async def ask_button(message: Message):
    await message.answer(
        "💬 Ask me anything!"
    )