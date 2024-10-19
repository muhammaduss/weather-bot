from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Узнать погоду")]],
    resize_keyboard=True,
)
