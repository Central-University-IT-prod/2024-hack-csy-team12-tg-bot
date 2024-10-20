import asyncio
import logging

from aiogram import F, Router, Bot, Dispatcher
from aiogram.filters import CommandStart,Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from bot.backend import add_queue_place, delete_queue_place, get_queue_statistic
from bot.keyboard import  main_keyboard_markup, start_main_keyboard

router: Router = Router()

from config import TOKEN

bot=Bot(token=TOKEN)
dp=Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Привет! Я бот, чем могу помочь?", reply_markup=start_main_keyboard)


@dp.message(lambda message: message.text == "Встать в очередь")
async def stand_in_queue(message: Message):
    await message.answer("Вы встали в очередь!" + add_queue_place(message.chat.id), reply_markup=main_keyboard_markup)

@dp.message(lambda message: message.text == "Отказаться от очереди")
async def stand_in_queue(message: Message):
    await message.answer("Вы отказались от очереди" + delete_queue_place(message.chat.id), reply_markup=start_main_keyboard)


@dp.message(lambda message: message.text == "Какой я в очереди?")
async def stand_in_queue(message: Message):
    await message.answer(get_queue_statistic(message.chat.id), reply_markup=start_main_keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ =='__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
