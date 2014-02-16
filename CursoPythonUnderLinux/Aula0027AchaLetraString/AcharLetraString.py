#!/usr/bin/env python
#-*- coding:utf8 -*-

frase = raw_input("Digite uma frase: ")
letra = raw_input("Digite a letra que deseja buscar: ")
cont  = len(frase)
print 'Cont é', cont
while cont > 0:
	if letra in frase[cont-1]:
		print 'letra encontrada'
		break
	else:
		print 'Ainda não achei \n'
		cont = cont - 1
else:
	print '''Busca finalizada, e a letra %s 
não foi encontrada na frase %s''' % (letra, frase)


