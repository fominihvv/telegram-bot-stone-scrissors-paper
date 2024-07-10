from random import choice
from lexicon.lexicon import LEXICON

player_win = {
    LEXICON['stone']: LEXICON['scissors'],
    LEXICON['scissors']: LEXICON['paper'],
    LEXICON['paper']: LEXICON['stone']}


def get_winner(human: str, bot: str) -> str:
    if human == bot:
        return 'draw'
    elif player_win[human] == bot:
        return 'player_win'
    else:
        return 'bot_win'


def get_bot_choice() -> str:
    return choice([LEXICON['stone'], LEXICON['scissors'], LEXICON['paper']])
