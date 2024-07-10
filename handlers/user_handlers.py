from lexicon.lexicon import LEXICON
from services.services import get_winner, get_bot_choice
from keyboards.keyboard import keyboard_yes_no, keyboard_game
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F
from models import methods
from config_data.config import logger


router_user_handlers = Router()


@router_user_handlers.message(CommandStart())
async def process_start_command(message: Message):
    logger.info(f'Пользователь {message.from_user.id} запустил бота')
    logger.debug(f'Проверяем наличие пользователя {message.from_user.id} в базе данных')
    user = await methods.get_user_data(message.from_user.id)
    if not user:
        logger.info(f'Создаем пользователя {message.from_user.id} в базе данных')
        await methods.new_user(message.from_user.id, [message.from_user.full_name, 0, 0, 0, 0])
    await message.answer(text=LEXICON['start_game'], reply_markup=keyboard_game)


@router_user_handlers.message(F.text.in_([LEXICON['stone'], LEXICON['scissors'], LEXICON['paper']]))
async def process_press_button(message: Message):
    logger.debug(f'Запрашиваем данные пользователя {message.from_user.id} в базе данных')
    user = await methods.get_user_data(message.from_user.id)
    player_choice = message.text
    await message.answer(text=LEXICON['player_choice'].format(player_choice))
    bot_choice = get_bot_choice()
    await message.answer(text=LEXICON['bot_choice'].format(bot_choice))
    result = get_winner(player_choice, bot_choice)
    await message.answer(text=LEXICON[result])
    user[2] += 1
    user[3] += result == 'player_win'
    user[4] += result == 'bot_win'
    user[5] += result == 'draw'
    logger.debug(f'Обновляем данные пользователя {message.from_user.id} в базе данных')
    await methods.update_user_data(message.from_user.id, user[2:])
    logger.debug(f'Показываем статистику пользователя {message.from_user.id}')
    await message.answer(text=LEXICON['stat'].format(*user[2:]))
    await message.answer(text=LEXICON['try_again'], reply_markup=keyboard_yes_no)


@router_user_handlers.message(F.text == LEXICON['yes'])
async def process_new_game(message: Message):
    logger.info(f'Пользователь {message.from_user.id} начал новую игру')
    await message.answer(text=LEXICON['start_game'], reply_markup=keyboard_game)


@router_user_handlers.message(F.text == LEXICON['no'])
async def process_new_game(message: Message):
    logger.info(f'Пользователь {message.from_user.id} закончил игру')
    await message.answer(text=LEXICON['goodbye'])
