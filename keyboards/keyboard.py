from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon import LEXICON

set_keyboard_game = [
    [KeyboardButton(text=LEXICON['stone']), KeyboardButton(text=LEXICON['scissors']),
     KeyboardButton(text=LEXICON['paper'])]]

set_keyboard_yes_no = [[KeyboardButton(text=LEXICON['no']), KeyboardButton(text=LEXICON['yes'])]]

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
