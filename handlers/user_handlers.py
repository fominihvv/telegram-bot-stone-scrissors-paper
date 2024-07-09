from lexicon.lexicon import LEXICON
from config_data.config import __LANG__
from services.services import get_winner, get_bot_choice
from keyboards.keyboard import keyboard_yes_no, keyboard_game
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F

router_user_handlers = Router()


@router_user_handlers.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON[__LANG__]['start_game'], reply_markup=keyboard_game)


@router_user_handlers.message(F.text.in_([LEXICON[__LANG__]['stone'],
                                          LEXICON[__LANG__]['scissors'],
                                          LEXICON[__LANG__]['paper']]))
async def process_press_button(message: Message):
    player_choice = message.text
    await message.answer(text=LEXICON[__LANG__]['player_choice'].format(player_choice))
    bot_choice = get_bot_choice()
    await message.answer(text=LEXICON[__LANG__]['bot_choice'].format(bot_choice))
    result = get_winner(player_choice, bot_choice)
    await message.answer(text=LEXICON[__LANG__][result])
    await message.answer(text=LEXICON[__LANG__]['try_again'], reply_markup=keyboard_yes_no)


@router_user_handlers.message(F.text == LEXICON[__LANG__]['yes'])
async def process_new_game(message: Message):
    await message.answer(text=LEXICON[__LANG__]['start_game'], reply_markup=keyboard_game)


@router_user_handlers.message(F.text == LEXICON[__LANG__]['no'])
async def process_new_game(message: Message):
    await message.answer(text=LEXICON[__LANG__]['goodbye'])
