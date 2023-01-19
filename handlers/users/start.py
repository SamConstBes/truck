from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.inline.main_menu import menu
from loader import dp
from utils.db_api.db_commands import create_client


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await create_client(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        name=message.from_user.first_name
    )
    await message.answer('Привет!', reply_markup=menu)
