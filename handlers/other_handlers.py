import logging
from lexicon.lexicon import LEXICON
from keyboards.keyboard import keyboard_yes_no
from aiogram.types import Message
from aiogram import Router

logger_user_handlers = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')

router_other_handlers = Router()


@router_other_handlers.message()
async def process_start_command(message: Message):
    logger_user_handlers.debug(f'Пользователь {message.from_user.id} ввёл неизвестную команду {message.text}')
    await message.answer(text=LEXICON['unknown_command'], reply_markup=keyboard_yes_no)
