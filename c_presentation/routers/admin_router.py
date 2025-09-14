from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from a_settings.config import settings

admin_router = Router()

# Пример фильтра для админов (дополните список своими ID)
ADMIN_IDS = {123456789}

@admin_router.message(Command("status"))
async def cmd_status(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        return
        
    await message.answer(
        f"✨ Статус бота:\n"
        f"Режим отладки: {settings.DEBUG}\n"
        f"Sheets API: {'Подключен' if settings.SHEETS_CREDENTIALS else 'Нет'}\n"
        f"Notion API: {'Подключен' if settings.NOTION_TOKEN else 'Нет'}"
    )