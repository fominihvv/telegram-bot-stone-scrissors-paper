from lexicon.lexicon import LEXICON
from services.services import get_winner, get_bot_choice
from keyboards.keyboard import keyboard_yes_no, keyboard_game
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F

router_user_handlers = Router()


@router_user_handlers.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['start_game'], reply_markup=keyboard_game)


@router_user_handlers.message(F.text.in_([LEXICON['stone'], LEXICON['scissors'], LEXICON['paper']]))
async def process_press_button(message: Message):
    player_choice = message.text
    await message.answer(text=LEXICON['player_choice'].format(player_choice))
    bot_choice = get_bot_choice()
    await message.answer(text=LEXICON['bot_choice'].format(bot_choice))
    result = get_winner(player_choice, bot_choice)
    await message.answer(text=LEXICON[result])
    await message.answer(text=LEXICON['try_again'], reply_markup=keyboard_yes_no)


@router_user_handlers.message(F.text == LEXICON['yes'])
async def process_new_game(message: Message):
    await message.answer(text=LEXICON['start_game'], reply_markup=keyboard_game)


@router_user_handlers.message(F.text == LEXICON['no'])
async def process_new_game(message: Message):
    await message.answer(text=LEXICON['goodbye'])
