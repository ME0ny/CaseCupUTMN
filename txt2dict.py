# -*- coding: utf8 -*-

f = open('tickets',encoding='utf-8', newline='')
symbol = 0
s = ''
g = open('tag.py','w',encoding='utf-8', newline='')
g.write('d = [')
for i in f:
    for j in i:
        if(j == '{'):
            symbol+=1
        if(j == '}'):
            symbol-=1
        s+=j
        if(symbol == 0):
            s+=',\n'
            g.write(s)
            s = ''
g.write('0]')
g.close()