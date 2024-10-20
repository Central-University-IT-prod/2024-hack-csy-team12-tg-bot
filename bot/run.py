import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart,Command
from aiogram.types import Message

from config import TOKEN

bot=Bot(token=TOKEN)
dp=Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hi')

@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Command /help')