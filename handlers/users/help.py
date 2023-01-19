from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.db_api.db_commands import get_client_telegram_id, get_all_clients


@dp.message_handler(Command('help'))
async def help_cmd(message: types.Message):
    data = await get_client_telegram_id(message.from_user.id)
    await message.answer(f'{data.telegram_id}\n'
                         f'{data.username}\n'
                         f'{data.name}')

    all_data = await get_all_clients()

    for i in range(len(all_data)):
        await message.answer(all_data[i].username)
