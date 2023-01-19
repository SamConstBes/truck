from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=3,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(text='Кнопка_1', callback_data='none'),
                                    InlineKeyboardButton(text='Кнопка_4', callback_data='none')
                                ],
                                [
                                    InlineKeyboardButton(text='Кнопка_2', callback_data='none')
                                ],
                                [
                                    InlineKeyboardButton(text='Кнопка_3', callback_data='none')
                                ]
                            ])