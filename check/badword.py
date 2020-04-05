'''
    Поиск нецензурной лексики
'''

#подкючение словаря нецензурной лексики
dictionary = open('badword.csv')
d ={}

#Создание словаря ключ-значение для дальнейшей работы
for line in dictionary:
    a = line.replace('\n','').split(';')
    d[a[0]]=a[1]
dictionary.close()


#Поиск слова в словаре 
def isBad(word):
    if word in d:
        return d[word] #возвращает вес слова, если она присутствует в словаре
    else:
        return 1 #возвращает единицу, если слова нет
