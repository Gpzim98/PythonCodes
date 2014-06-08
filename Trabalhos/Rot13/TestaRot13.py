#!/usr/bin/env python
# coding: utf-8

# Importando as funcoes do arquivo que tem todas as funcoes (Funcao.py)
from Funcao import Rot13

# Execucao inicial
# Aqui estamos montando o menu que sera mostrado para o usuario
MENU = """
	1 - Para testar com Dicionarios{}\n
	2 - Para testar com Listas[]\n
	3 - Para testar com Tuplas()\n
	4 - Para testar com Strings ' ' \n
	5 - Para testar com 2 Listas [] \n
	6 - Para testar com 2 Strings ' ' \n
	7 - Criptografar um arquivo (.txt) ' ' \n
	8 - Criptografar usando a função Maketrans ' ' \n

	DIGITE A OPCAO ESCOLHIDA: 
"""
# Variavel que determina se o programa continua executando
continua = 'sim'

# a variavel C e a que pode chamar as funcoes do arquivo Funcoao.py
c = Rot13()

#Aqui um loop comum pra ficar perguntando ao usuario se ele quer continuar executando o programa
while continua == 'sim':
	# Imprimo o menu e pego a opcao que ele escolheu
	opc = raw_input(MENU)

	# De acorco com a escolha do usuario, vai entrar em um destes ifs e chamar a funcao correpondentem Funcao.py
	if opc == '1':
		resultado = c.encripta_dicionario(raw_input("Digite uma frase para ser criptografada: "))
		print resultado
	elif opc == '2':
		resultado = c.encripta_lista(raw_input("Digite uma frase para ser criptografada: "))
		print resultado
	elif opc == '3':
		resultado = c.encripta_tupla(raw_input("Digite uma frase para ser criptografada: "))
		print resultado
	elif opc == '4':
		resultado = c.encripta_string(raw_input("Digite uma frase para ser criptografada: "))
		print resultado
	elif opc == '5':
		resultado = c.encripta_com_2_listas(raw_input("Digite uma frase para ser criptografada: ").lower())
		print resultado
	elif opc == '6':
		resultado = c.encripta_com_2_strings(raw_input("Digite uma frase para ser criptografada: "))
		print resultado
	elif opc == '7':
		# Pergunta ao usuario se ele quer mostrar o arquivo criptografado no final
		mostra_tela = raw_input('Digite MOSTRAR para que ao final seja exibido o arquivo original e o criptografado: ').lower()		
		c.abre_arquivo_criptografa(raw_input('Informe o caminho do arquivo a ser criptografado: '), (mostra_tela == 'mostrar'))
	elif opc == '8':
		c.encripta_maketrans(raw_input("Digite uma frase para ser criptografada: "))
	else:
		print 'Opcao invalida'
	continua = raw_input('Digite sim para continuar ... ')
# Caso o usuario nao digite SIM para continuar a execucao do programa ele sai
else:
	print 'Bye :p'