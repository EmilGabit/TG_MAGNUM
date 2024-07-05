from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from keybords.keybords import language_kb, create_article_keybord
from lexicon.lexicon import LEXICON_RU
from date_base.date_base import users
from services.services import wiki_language, search_wiki
import wikipedia

router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            'in_work': True,
            'language' : '',
        }


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


# Этот хэндлер срабатывает на команду /language
@router.message(Command(commands='language'))
async def process_language_command(message: Message):
    await message.answer(text=LEXICON_RU['/language'], reply_markup = language_kb)



# Этот хэндлер срабатывает на команду /stat
@router.message(Command(commands='stat'))
async def process_help_command(message: Message):
    await message.answer(f"{LEXICON_RU['lang']} {LEXICON_RU[users[message.from_user.id]['language']]}\n"
                         f"{LEXICON_RU['search']} {users[message.from_user.id]['search']}\n"
                         )

# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'ru'
@router.callback_query(F.data == 'ru')
async def process_button_press(callback: CallbackQuery):
    wiki_language(callback.data)
    users[callback.from_user.id]['language'] = callback.data
    await callback.answer(
        text=LEXICON_RU['ru_button'],
        show_alert=True)


@router.callback_query(F.data == 'en')
async def process_button_press(callback: CallbackQuery):
    wiki_language(callback.data)
    users[callback.from_user.id]['language'] = callback.data
    await callback.answer(
        text=LEXICON_RU['en_button'],
        show_alert=True)


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
@router.callback_query(F.data)
async def process_call_back_query_press(callback: CallbackQuery):
    article = callback.data
    respon = search_wiki(article)
    if type(respon) == list:
        await callback.message.edit_text(text=LEXICON_RU['choice'],
                             reply_markup=create_article_keybord(respon))
    elif type(respon) == str:
        await callback.message.edit_text(text=respon)



