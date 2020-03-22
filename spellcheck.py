'''
    Проверка  текста на орфографию
'''
# coding: utf-8
from spellchecker import SpellChecker

#Подсчет количества орфографических ошибок в тексте
def find_misspells(text):

    # Загрузка модели
    spell = SpellChecker(language=None, case_sensitive=False)

    # Подключение словаря
    spell.word_frequency.load_dictionary('my_custom_dictionary.gz')

    #Стандартизация данных
    formalized_splitted_text = text.replace('.', '').replace(',','').replace('?','').replace('!','').split()

    #Подсчет количества слов в тексте
    words_qty = len(formalized_splitted_text)
    
    #Поиск ошибок в тексте
    misspells = spell.unknown(formalized_splitted_text)

    #Подсчет количества ошибок
    misspells_qty = len(misspells)
    fin_text = ''

    #Сохранение текста без ошибок для дальнейшей работы
    for word in formalized_splitted_text:
        if word in misspells:
            fin_text+=spell.correction(word)+' '
        else:
            fin_text+=word+' '

    #Передаем обратно список из 
    return [
        fin_text, #измененного текста, только правильно написанные слова
        words_qty,#количество слов в сообщение 
        misspells_qty#количество допущенных ошибок
    ]



