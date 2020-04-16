'''
    Главный файл
    Выводит оценку текста менеджера
'''

# coding: utf-8
from spellcheck import find_misspells # Подклюсение функции проверки орфографии
import badword,subjects       # Подключение функций: проверка нецензурной лексики, проверка уместности ответа

data = ['Хочу купить билет по скидке. А есть субсидии для студентов? Москва Владивосток','Мы не летаем в этым напровлении!']

#Функция нормализации данных. Данные нормализуются в значения от 0 до 1
def norm(allLen,mis): 
    out = ((mis-(allLen/allLen+1))/(allLen-(allLen/allLen+1)))
    if out<0:
        return 0
    else:
        return out

weightSpell = 0.2 #Вес для оценки орфографии
weightSub = 0.8   #Вес для оценки показателя "Уместность ответа"
valueSpell = 0    #Балл, который показывает, насколько много орфографических ошибок допустил клиент
valueSub = 0      #Балл, который показывает, насколько уместен, точен был ответ
question = data[0]     #Вопрос клиента, считается, что первое сообщение это вопрос
answers = []      #Список для хранения всех ответов менеджера

#извелечение вопроса из сообщений клиента


answers.append(data[1]) #извелечение всех сообщений менеджера
answersWords = '' #Строка исправленных сообщений
answersFirst = '' #Первый ответ
count = 0 #Счетчик количества ответов
summ = 0  #Сумма всех баллов за орфографию

#Поиск орфографических ошибок в сообщениях
for i in answers:
    r = find_misspells(i)
    print(r)
    answersWords+=r[0]+' '
    if count == 0:
        answersFirst = r[0]
    count+=1
    summ+=(1-norm(r[1],r[2]))

valueSpell = weightSpell*(summ/count)#Параметр, указывающий на количество ошибок во всем диалоге (от 0 до 0.2).
                                     #Считается, как среднеарифметическое значение баллов в каждом предложении умноженное на вес 0.2



weightBad = 1 #Параметр, указывающий на количество нецензурной лексики, максимальное значение 1

#поиск нецензурной лексики, все значения перемножаются
for i in answersWords:
    weightBad*=badword.isBad(i)
print(question)
print(answersFirst)
valueSub = (subjects.overlaps(question,answersFirst)/100)*weightSub #Подсчет баллов за уместность ответа на вопрос (0 - 0.8)
print(valueSpell)
valueSub = 0.8
print('Программа оценивает работу менеджера на',float('{:.2f}'.format(((valueSpell+valueSub)*weightBad*5)))) #вывод оценки

#формула оценки 
#(Балл за орфографию + Балл за уместность ответа)*Вес за нецензурную лексику или эмоцианально окрашенную * на 5 для стандартизации


