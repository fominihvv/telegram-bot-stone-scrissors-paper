import asyncio
import logging
from dataclasses import dataclass
from environs import Env

logger_config = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')

db_lock = asyncio.Lock()


@dataclass
class LocalDatabaseConfig:
    database: str
    database_path: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot
    db: LocalDatabaseConfig


def load_config(path: str | None = None) -> Config:
    try:
        logger_config.info('Загрузка конфигурации из .env')
        env: Env = Env()
        env.read_env(path)
    except FileNotFoundError:
        logger_config.critical('Файл .env отсутствует. Программа будет остановлена')
        raise SystemExit

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=env.list('ADMIN_IDS')
        ),
        db=LocalDatabaseConfig(
            database=env('database'),
            database_path=env('database_path')
        )
    )


config = load_config('.env')
