import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

# Завантажуємо змінні з .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


async def echo_handler(message: Message):
    """Ехо-бот: відповідає тим самим повідомленням"""
    await message.answer(message.text)


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Обробник усіх текстових повідомлень
    dp.message.register(echo_handler)

    print("Бот запущений...")
    await dp.start_polling(bot)


if name == "main":
    asyncio.run(main())