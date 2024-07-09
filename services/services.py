from random import choice
from lexicon.lexicon import LEXICON
from config_data.config import __LANG__

player_win = {
    LEXICON[__LANG__]['stone']: LEXICON[__LANG__]['scissors'],
    LEXICON[__LANG__]['scissors']: LEXICON[__LANG__]['paper'],
    LEXICON[__LANG__]['paper']: LEXICON[__LANG__]['stone']}


def get_winner(human: str, bot: str) -> str:
    if human == bot:
        return 'draw'
    elif player_win[human] == bot:
        return 'player_win'
    else:
        return 'bot_win'


def get_bot_choice() -> str:
    return choice([LEXICON[__LANG__]['stone'], LEXICON[__LANG__]['scissors'], LEXICON[__LANG__]['paper']])
