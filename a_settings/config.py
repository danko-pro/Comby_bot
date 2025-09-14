"""
Модуль конфигурации приложения.
Отвечает за загрузку и управление настройками бота из переменных окружения.
Использует паттерн Singleton через единственный экземпляр класса Settings.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
import os

# Загружаем .env файл из директории с настройками
ENV_PATH = Path(__file__).parent / '.env'
load_dotenv(ENV_PATH)

@dataclass
class Settings:
    """
    Класс настроек приложения, загружаемых из переменных окружения.
    
    Атрибуты:
        BOT_TOKEN (str): Токен бота Telegram, обязательный параметр для работы
        PROJECT_NAME (str): Название проекта, используется в логах и сообщениях
        DEBUG (bool): Режим отладки, влияет на уровень логирования и подробность ошибок
        SHEETS_CREDENTIALS (Optional[Path]): Путь к файлу креденшелов Google Sheets API
        NOTION_TOKEN (Optional[str]): Токен для интеграции с Notion API
    
    Примечание:
        Все настройки можно переопределить через переменные окружения
        Значения по умолчанию используются, если переменная не найдена
    """
    # Настройки бота
    BOT_TOKEN: str = os.getenv('BOT_TOKEN', '')
    
    # Общие настройки проекта
    PROJECT_NAME: str = 'Your Bot'
    DEBUG: bool = os.getenv('DEBUG', 'False').lower() in ('1', 'true', 'yes')
    
    # Настройки внешних интеграций
    SHEETS_CREDENTIALS: Optional[Path] = Path(os.getenv('SHEETS_CREDENTIALS', '')) or None
    NOTION_TOKEN: Optional[str] = os.getenv('NOTION_TOKEN', '') or None

# Создаем единственный экземпляр настроек для использования во всем приложении
settings = Settings()