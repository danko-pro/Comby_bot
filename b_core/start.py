"""
Точка входа в приложение.
Этот модуль инициализирует и запускает Telegram бота.
Настраивает логирование, создает экземпляр бота и диспетчера,
и запускает long polling для получения обновлений от Telegram.
"""

import asyncio
import logging

from b_core.bot_manager import create_bot_and_dispatcher

async def main():
    """
    Основная асинхронная функция приложения.
    
    Выполняет следующие шаги:
    1. Настраивает систему логирования
    2. Создает экземпляры бота и диспетчера
    3. Запускает получение обновлений от Telegram
    4. Корректно закрывает сессию при завершении
    
    Raises:
        Exception: Любые исключения при работе бота логируются
                  и приводят к корректному завершению сессии
    """
    # Настройка системы логирования с отметками времени
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Создание бота и диспетчера сообщений
    bot, dp = create_bot_and_dispatcher()
    
    # Запуск получения обновлений от Telegram
    try:
        # Запускаем long polling в бесконечном цикле
        await dp.start_polling(bot)
    finally:
        # Гарантируем закрытие сессии даже при ошибках
        await bot.session.close()

if __name__ == '__main__':
    # Запуск асинхронной функции в синхронном контексте
    asyncio.run(main())