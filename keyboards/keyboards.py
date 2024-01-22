from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# !!! Create yes-no-keyboard using Builder

# Creating buttons with agreement and disagriiment to play the game
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# Initialise Builder for keyboard with bauttons Let's go ang Don't want
yes_no_kb_builder = ReplyKeyboardBuilder()

# Add buttons to builder
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Create keyboard with bauttons Let's go ang Don't want
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True, # keyboard has to vanish after user presses it
    resize_keyboard=True,
)


# !!! Create playing keyboard without Builder

# Create buttons
button_1 = KeyboardButton(text=LEXICON_RU['stone'])
button_2 = KeyboardButton(text=LEXICON_RU['scissors'])
button_3 = KeyboardButton(text=LEXICON_RU['paper'])

# Create keyboards
game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1], [button_2], [button_3]],
    resize_keyboard=True
)