from aiogram.dispatcher.filters.state import StatesGroup, State


class GetInfo(StatesGroup):
    q1 = State()