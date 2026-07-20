from aiogram import Router
from aiogram.types import Message

from keyboards.main import main_keyboard


router = Router()


@router.message(lambda message: message.text == "📚 Help")
async def help_button(message: Message):
    await message.answer(
        "📚 Cyrus Assistant Commands:\n\n"
        "🚀 Basic:\n"
        "/start - Start the bot\n"
        "/help - Show this menu\n"
        "/about - About Cyrus\n\n"

        "🛠️ Utility:\n"
        "/ping - Check bot status\n"
        "/id - Show your Telegram ID\n"
        "/userinfo - Show your profile info\n"
        "/time - Show current time"
    )


@router.message(lambda message: message.text == "ℹ️ About")
async def about_button(message: Message):
    await message.answer(
        "ℹ️ About Cyrus\n\n"
        "Cyrus is a Telegram assistant built with Python and Aiogram."
    )


@router.message(lambda message: message.text == "🤖 Ask Cyrus")
async def ask_button(message: Message):
    await message.answer(
        "🤖 AI features are currently disabled.\n\n"
        "Try using /help to see available commands."
    )