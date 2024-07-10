import aiosqlite
import logging
import database.db_query as db_query
from config_data.config import config, db_lock


logger_user_db_methods = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')


async def db_check() -> None:
    logger_user_db_methods.info('Создание таблицы в базе данных если она отсутствует')
    logger_user_db_methods.debug(f'Ждём {db_lock}')
    async with db_lock:
        async with aiosqlite.connect(f'{config.db.database_path}/{config.db.database}') as connection:
            cursor = await connection.cursor()
            await cursor.execute(db_query.create_new_table)
            await connection.commit()


async def get_user_data(user_id: int) -> list:
    logger_user_db_methods.info(f'Получение данных пользователя {user_id} из базы данных')
    logger_user_db_methods.debug(f'Ждём {db_lock}')
    async with db_lock:
        async with aiosqlite.connect(f'{config.db.database_path}/{config.db.database}') as connection:
            cursor = await connection.cursor()
            await cursor.execute(db_query.get_user_data, (user_id,))
            result = await cursor.fetchone()
            if result is None:
                return []
            else:
                return list(result)


async def update_user_data(user_id: int, user: list) -> None:
    logger_user_db_methods.info(f'Сохранение данных пользователя {user_id} в базе данных')
    logger_user_db_methods.debug(f'Ждём {db_lock}')
    async with db_lock:
        async with aiosqlite.connect(f'{config.db.database_path}/{config.db.database}') as connection:
            cursor = await connection.cursor()
            await cursor.execute(db_query.update_user_data, (*user, user_id))
            await connection.commit()


async def new_user(user_id: int, user: list) -> None:
    logger_user_db_methods.info(f'Добавление нового пользователя {user_id} в базу данных')
    logger_user_db_methods.debug(f'Ждём {db_lock}')
    async with db_lock:
        async with aiosqlite.connect(f'{config.db.database_path}/{config.db.database}') as connection:
            cursor = await connection.cursor()
            await cursor.execute(db_query.new_user, (user_id, *user))
            await connection.commit()
