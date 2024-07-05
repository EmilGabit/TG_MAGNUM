from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from lexicon.lexicon import LEXICON_RU

# Создаем кнопки с ответами орел, решка и отказа
ru_button = InlineKeyboardButton(text=LEXICON_RU['ru'],  callback_data='ru')
en_button = InlineKeyboardButton(text=LEXICON_RU['en'],  callback_data='en')

# Создаем объект инлайн-клавиатуры
language_kb = InlineKeyboardMarkup(
    inline_keyboard=[[ru_button],
                     [en_button]]
)


def create_article_keybord(buttons: list) -> InlineKeyboardMarkup:
    for button in buttons:
        button = InlineKeyboardButton(text=str(button), callback_data=str(button))
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    # Добавляем в билдер ряд с кнопками
    kb_builder.row(*[InlineKeyboardButton(
        text=button, callback_data=button) for button in buttons], width=1
                   )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup(one_time_keyboard=True,
    resize_keyboard=True)

