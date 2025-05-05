
import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.markdown import hbold

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(commands=["start"])
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {hbold(message.from_user.full_name)}! Kodni yuboring:")

@dp.message()
async def handle_message(message: Message):
    code = message.text.strip().upper()
    if code.startswith("KITOB-100"):
        await message.answer("Bu Dinleme kitobi uchun kanal: https://t.me/+UsgfmN3A9VY5YTE6")
    elif code.startswith("KITOB-200"):
        await message.answer("Bu Konuşma kitobi uchun kanal: https://t.me/+gLNjPeGxsh1iZWYy")
    else:
        await message.answer("Kod noto‘g‘ri. Iltimos, qayta urinib ko‘ring.")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
