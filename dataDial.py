# -*- coding: utf8 -*-
from dict2dialog import dialog

f = open('data2.txt','w',encoding='utf-8', newline='')

f.write(dialog())
f.close()