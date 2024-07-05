import wikipedia
from lexicon.lexicon import LEXICON_RU


#написать функцию, которая будет менять язык
def wiki_language(lang: str):
    wikipedia.set_lang(lang)



def search_wiki(text: str):
    article = str(text)
    try:
        options = wikipedia.page(article)
    except wikipedia.exceptions.PageError as err:
        return LEXICON_RU['none_article']
    except wikipedia.exceptions.DisambiguationError as opti:
        return opti.options
    else:
        ny = wikipedia.page(article)
        if len(ny.summary) <= 1000:
            ny_text = ny.summary
        else:
            ny_text = ny.summary[:997] + "... <b>Для просмотра полной статьи перейдите по источнику:</b>"
        return f'{ny.title}\n{ny_text}\n\n{ny.url}'


