#!/usr/bin/env python

from Funcao import Rot13
def testa_dicionario():
	dicionario = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':21,'w':23,'x':24,'y':25,'z':26}
	c = Rot13()
	for i in dicionario:
		print c.encripta(i)

def testa_lista():		
	lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	c = Rot13()
	for i in lista:
		print c.encripta(i)

def testa_tupla():		
	tupla = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	c = Rot13()
	for i in tupla:
		print c.encripta(i)

def testa_string():		
	#Opcional: Com letras maiusculas e minusculas
	string = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
	c = Rot13()
	for i in string:
		print c.encripta(i)

def testa_2_listas():		
	lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',   'k', 'l', 'm']
	lista2 = ['n', 'o', 'p', 'q', 'r', 's', 't',  'u', 'v','w', 'x', 'y', 'z']

	c = Rot13()

	[(c.encripta(x),c.encripta(y)) for x in lista1 for y in lista2]
	###???????
		
# Execucao inicial
MENU = """
	1 - Para testar com Dicionarios{}\n
	2 - Para testar com Listas[]\n
	3 - Para testar com Tuplas()\n
	4 - Para testar com Strings ' ' \n
	5 - Para testar com 2 Strings ' ' \n

	DIGITE A OPCAO ESCOLHIDA: 
"""
continua = 'sim'

while continua == 'sim':
	opc = raw_input(MENU)

	if opc == '1':
		testa_dicionario()		
	elif opc == '2':
		testa_lista()
	elif opc == '3':
		testa_tupla()
	elif opc == '4':
		testa_string()
	elif opc == '5':
		testa_2_listas()
	else:
		print 'Opcao invalida'
	continua = raw_input('Digite sim para continuar ... ')
else:
	print 'Bye :p'