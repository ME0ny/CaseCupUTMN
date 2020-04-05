'''
    Главный файл
    Выводит оценку текста менеджера
'''

# coding: utf-8
from spellcheck import find_misspells # Подклюсение функции проверки орфографии
import badword,subjects       # Подключение функций: проверка нецензурной лексики, проверка уместности ответа
from txt2dict import convert
from tag import d
from dict2dialog import dialog
from nlp import recognition

#Функция нормализации данных. Данные нормализуются в значения от 0 до 1
def norm(allLen,mis): 
    out = ((mis-(allLen/allLen+1))/(allLen-(allLen/allLen+1)))
    if out<0:
        return 0
    else:
        return out

'''
    Принимает на вход только один тикет
    Считает балл за диалог
'''
def main(ticket):
    #файлы с текстовыми сообщениями разговора. Каждая новая строчка - весь текст до ответа
    convert(ticket)#преобразование тикета в словарь для работы в python
    data= dialog()#получение данных представленных 
    client = data[0]
    operator = data[1]


    weightSpell = 0.2 #Вес для оценки орфографии
    weightSub = 0.8   #Вес для оценки показателя "Уместность ответа"
    valueSpell = 0    #Балл, который показывает, насколько много орфографических ошибок допустил клиент
    valueSub = 0      #Балл, который показывает, насколько уместен, точен был ответ
    question = ''     #Вопрос клиента, считается, что первое сообщение это вопрос
    answers = []      #Список для хранения всех ответов менеджера

    answersWords = '' #Строка исправленных сообщений
    answersFirst = '' #Первый ответ
    count = 0 #Счетчик количества ответов
    summ = 0  #Сумма всех баллов за орфографию

    #Поиск орфографических ошибок в сообщениях
    for i in operator:
        r = find_misspells(i)
        answersWords+=r[0]+' '
        count+=1
        summ+=(1-norm(r[1],r[2]))

    valueSpell = weightSpell*(summ/count)#Параметр, указывающий на количество ошибок во всем диалоге (от 0 до 0.2).
                                        #Считается, как среднеарифметическое значение баллов в каждом предложении умноженное на вес 0.2

    weightBad = 1 #Параметр, указывающий на количество нецензурной лексики, максимальное значение 1
    badwordArray = []
    #поиск нецензурной лексики, все значения перемножаются
    for i in answersWords:
        badwordValue = badword.isBad(i)
        if badwordValue[0]==1:
            weightBad*=1
        else:
            weightBad = badwordValue[0]
            badwordArray.append(badwordValue[1])

    valueSub = (subjects.overlaps(question,answersFirst)/100)*weightSub #Подсчет баллов за уместность ответа на вопрос (0 - 0.8)

    client_labels = []
    operator_labels = []
    valueNLP = 0
    for i in client:
        client_labels.append(recognition(i))
    for i in operator:
        operator_labels.append(recognition(i))
    for i in range(len(operator_labels)):
        if(operator_labels[i]==client_labels[i]):
            valueNLP+=1
    weightNLP = valueNLP/len(operator_labels)*5

    return ['Программа оценивает работу менеджера на ' + str(float('{:.2f}'.format(((valueSpell+valueSub)*weightBad*5)))), r[4],weightNLP,badwordArray,client,operator] #вывод оценки

    #формула оценки 
    #(Балл за орфографию + Балл за уместность ответа)*Вес за нецензурную лексику или эмоцианально окрашенную * на 5 для стандартизации



