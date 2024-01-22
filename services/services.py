import random

from lexicon.lexicon_ru import LEXICON_RU

# The function creates bot's choice.
def get_bot_choice() -> str:
    return random.choice(['stone', 'scissors', 'paper'])

# The function gets user's choice from lexicon dictionary.
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key

# The funtrion picks a winner
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules = {'stone': 'scissors',
             'scissors': 'paper',
             'paper': 'stone'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'