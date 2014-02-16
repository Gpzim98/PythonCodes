#!/usr/bin/env python
#-*- coding:utf8 -*-

frase = raw_input('Digite uma frase: ')
pos = 0
count = 0
while pos < len(frase):
    if ' ' in frase[pos]:
        count += 1
    pos += 1
print '\nEspacos vazios = %i' % (count)
