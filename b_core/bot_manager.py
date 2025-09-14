"""
Модуль управления ботом.
Отвечает за создание и настройку экземпляров бота и диспетчера.
Здесь настраиваются основные компоненты бота: парсинг сообщений,
хранилище состояний и подключение роутеров.
"""

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from a_settings.config import settings
from c_presentation.routers import router as collected_router

def create_bot_and_dispatcher() -> tuple[Bot, Dispatcher]:
    """
    Создает и настраивает экземпляры бота и диспетчера.
    
    Returns:
        tuple[Bot, Dispatcher]: Кортеж из настроенных экземпляров бота и диспетчера
        
    Notes:
        - Бот настраивается на использование HTML разметки по умолчанию
        - Используется MemoryStorage для хранения состояний FSM
        - Все роутеры из c_presentation автоматически подключаются к диспетчеру
    """
    # Создаем экземпляр бота с настройками по умолчанию
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    
    # Создаем хранилище состояний в памяти для FSM (машины состояний)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Подключаем все роутеры из слоя представления
    dp.include_router(collected_router)
    
    return bot, dp