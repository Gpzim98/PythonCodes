#!/usr/bin/env python
# -*- coding:utf8 -*-

cont = 1
lista = []
while cont <= 6:
	lista.append(input("Digite qualquer coisa: "))
	cont = cont + 1

print lista
for item in lista:
	if (type(item) == int):
		print 'Item inteiro: %d' % item

	elif (type(item) == str):
		print 'Item string %s ' % item

	elif (type(item) == float):
		print 'Item float %s ' % item
								
	elif (type(item) == list):
		print 'Item lista %s ' % item
								
	elif (type(item) == tuple):
		print 'Item tupla %s ' % item
								
	elif (type(item) == dict):
		print 'Item lista %s ' % item
								
