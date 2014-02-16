#!/usr/bin/env python
#-*- coding:utf8 -*-
media = 0
count = 4
while count != 0:
    valor = int(raw_input('Digite um valor: '))
    media = media + valor
    if count == 1:
        media /= 4
    count -= 1
print 'A media dos valores e %i' %(media)
