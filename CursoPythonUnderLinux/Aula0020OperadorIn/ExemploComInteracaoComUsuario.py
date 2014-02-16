#!/usr/bin/env python
#-*- coding:utf8 -*-

lista = [1, 2, 3, 4, 5]
item = int(raw_input('Escolha um numero dentro da seguinte lista:\n'+str(lista)+'\n'))
if item in lista:
    print 'Você escolheu',str(item)
else:
    print 'Este numero nao esta na lista'
