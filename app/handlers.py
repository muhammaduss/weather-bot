import app.keyboards as kb
import requests
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.weather import Weather
from configs.config import API_TOKEN, API_URL

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Это бот который вернет информацию о погоде в указанном "
        + "городе. Нажмите на 'Узнать погоду'",
        reply_markup=kb.main,
    )


@router.message(F.text == "Узнать погоду")
async def check_weather(message: Message, state: FSMContext):
    await state.set_state(Weather.city)
    await message.answer("Введите город, в котором вы хотите узнать погоду:")


@router.message(Weather.city)
async def get_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    data = await state.get_data()

    query = API_URL + "&appid=" + API_TOKEN + "&q=" + data["city"]
    print(query)
    response = requests.get(query, timeout=10)

    await message.answer(f"Yout city is: {response.json()}")
    await state.clear()
