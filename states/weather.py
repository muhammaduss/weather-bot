from aiogram.fsm.state import State, StatesGroup


class Weather(StatesGroup):
    city = State()
