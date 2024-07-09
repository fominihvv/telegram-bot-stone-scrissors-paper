from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon import LEXICON
from config_data.config import __LANG__

set_keyboard_game = [
    [KeyboardButton(text=LEXICON[__LANG__]['stone']), KeyboardButton(text=LEXICON[__LANG__]['scissors']),
     KeyboardButton(text=LEXICON[__LANG__]['paper'])]]

set_keyboard_yes_no = [[KeyboardButton(text=LEXICON[__LANG__]['no']), KeyboardButton(text=LEXICON[__LANG__]['yes'])]]

keyboard_game = ReplyKeyboardMarkup(
    keyboard=set_keyboard_game,
    resize_keyboard=True,
    one_time_keyboard=True
)

keyboard_yes_no = ReplyKeyboardMarkup(
    keyboard=set_keyboard_yes_no,
    resize_keyboard=True,
    one_time_keyboard=True
)
