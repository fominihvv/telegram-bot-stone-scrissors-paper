import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import config
from handlers import user_handlers
from database import db_methods


async def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Настраиваем переменные окружения')
    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()

    logger.info('Проверяем наличие базы данных')
    await db_methods.db_check()

    logger.info('Регистрируем роутеры в диспетчере')
    dp.include_router(user_handlers.router_user_handlers)

    logger.info('Удаляем старые апдейты')
    await bot.delete_webhook(drop_pending_updates=True)

    logger.info('Запускаем бота')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
