from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤖 Ask Cyrus"),
        ],
        [
            KeyboardButton(text="📚 Help"),
            KeyboardButton(text="ℹ️ About"),
        ],
    ],
    resize_keyboard=True
)