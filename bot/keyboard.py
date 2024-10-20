from aiogram.types import (ReplyKeyboardmarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardmarkup(keyboard=[
    [KeyboardButton(text='Каталог')]
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
],
                            resize_keyboard=True
                            input_field_placeholder='Выберите пункт меню')

seetings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YT')]
    ])

cras = ['Tesla', 'Merc', 'BMW']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car))
    return keyboard.adjust(2).as_markup()