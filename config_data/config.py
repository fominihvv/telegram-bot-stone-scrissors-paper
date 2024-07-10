import asyncio
import logging
from dataclasses import dataclass
from environs import Env

logger = logging.getLogger(__name__)
db_lock = asyncio.Lock()


@dataclass
class LocalDatabaseConfig:
    database: str  # Название базы данных
    database_path: str  # Путь к базе данных


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot
    db: LocalDatabaseConfig


def load_config(path: str | None = None) -> Config:
    try:
        logger.info('Загрузка конфигурации из .env')
        env: Env = Env()
        env.read_env(path)
    except FileNotFoundError:
        logger.critical('Файл .env отсутствует. Программа будет остановлена')
        raise SystemExit

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')
        ),
        db=LocalDatabaseConfig(
            database=env('database'),
            database_path=env('database_path')
        )
    )

config = load_config('.env')