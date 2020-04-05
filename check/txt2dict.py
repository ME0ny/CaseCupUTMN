# -*- coding: utf8 -*-
'''
    Конвертируем данные
'''
def convert(ticket):
    symbol = 0
    flag = False
    s = ''
    g = open('tag.py','w',encoding='utf-8', newline='')
    g.write('d = [')
    for j in ticket:
        if(j == '{'):
            flag = True
            symbol+=1
        if(j == '}'):
            symbol-=1
        s+=j
        if(symbol == 0 and flag == True):
            flag = False
            s+=','
            g.write(s)
            s = ''
    g.write('0]\n')
    g.close()