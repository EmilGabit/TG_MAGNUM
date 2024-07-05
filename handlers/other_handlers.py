from aiogram import Router, F
from aiogram.types import Message, ContentType
from lexicon.lexicon import LEXICON_RU
from services.services import search_wiki
from keybords.keybords import create_article_keybord
from date_base.date_base import users

router = Router()

#Хэндлер для сообщений которые не являются текстом
@router.message(F.content_type.in_({ContentType.PHOTO, ContentType.VOICE, ContentType.VIDEO, ContentType.AUDIO}))
async def other_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])

# Хэндлер для сообщений типа текст
@router.message(F.text)
async def send_answer(message: Message):
    respon =  search_wiki(message.text)
    if type(respon) == list:
        await message.answer(text=LEXICON_RU['choice'],
                             reply_markup=create_article_keybord(respon))
    elif type(respon) == str:
        await message.answer(text=respon)

@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(text=LEXICON_RU['response'] ,chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text=LEXICON_RU['response']
        )




