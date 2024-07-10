import aiosqlite
import models.db_query as db_query
from config_data.config import config, logger, db_lock


async def db_check() -> None:
    logger.info('Создание таблицы в базе данных если она отсутствует')
    logger.debug(f'Ждём {db_lock}')
    async with db_lock:
        async with aiosqlite.connect(f'{config.db.database_path}/{config.db.database}') as connection:
            cursor = await connection.cursor()
            await cursor.execute(db_query.create_new_table)
            await connection.commit()


async def get_user_data(user_id: int) -> list:
    logger.info(f'Получение данных пользователя {user_id} из базы данных')
    logger.debug(f'Ждём {db_lock}')
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
    logger.info(f'Сохранение данных пользователя {user_id} в базе данных')
    logger.debug(f'Ждём {db_lock}')
    async with db_lock:
        async with aiosqlite.connect(f'{config.db.database_path}/{config.db.database}') as connection:
            cursor = await connection.cursor()
            await cursor.execute(db_query.update_user_data, (*user, user_id))
            await connection.commit()


async def new_user(user_id: int, user: list) -> None:
    logger.info(f'Добавление нового пользователя {user_id} в базу данных')
    logger.debug(f'Ждём {db_lock}')
    async with db_lock:
        async with aiosqlite.connect(f'{config.db.database_path}/{config.db.database}') as connection:
            cursor = await connection.cursor()
            await cursor.execute(db_query.new_user, (user_id, *user))
            await connection.commit()
