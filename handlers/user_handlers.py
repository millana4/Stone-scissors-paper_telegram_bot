from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner

router = Router()

# The handler works when /start has been pressed
@router.message(CommandStart())
async  def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)

# The handler works when /help has been pressed
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)

# The handler works when Yes has been pressed
@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(massage: Message):
    await massage.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)

# The handler works when No has been pressed
@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])

# The handler works when any game button has been pressed
@router.message(F.text.in_([LEXICON_RU['stone'],
                            LEXICON_RU['scissors'],
                            LEXICON_RU['paper'],]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                         f'— {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)
