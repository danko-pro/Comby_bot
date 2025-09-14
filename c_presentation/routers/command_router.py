from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

command_router = Router()

@command_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Привет! Я ваш бот-помощник.\n"
        "Используйте /help для списка команд."
    )

@command_router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "📝 Доступные команды:\n"
        "/start - Начать работу\n"
        "/help - Показать это сообщение"
    )