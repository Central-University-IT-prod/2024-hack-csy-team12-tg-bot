from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

start_keyboard = [
[KeyboardButton(text='Встать в очередь')]
]

main_keyboard = [
    [KeyboardButton(text='Отказаться от очереди')],
    [KeyboardButton(text='Какой я в очереди?')]
]

start_main_keyboard = ReplyKeyboardMarkup(keyboard=start_keyboard,
                                    resize_keyboard=True,
                                    input_field_placeholder='Выберите пункт меню')

main_keyboard_markup = ReplyKeyboardMarkup(keyboard=main_keyboard,
                                    resize_keyboard=True,
                                    input_field_placeholder='Выберите пункт меню')

