#!/usr/bin/env python
# coding: utf-8
import FuncoesCriptografia

# Monta o menu que será mostrado ao usuário
# Na variavel escolha é colocada a opção escolhida
executar  = raw_input("""
			a - ROOT13 COM DICIONARIO \n
			b - ROOT13 COM LISTAS \n
			c - ROOT13 COM STRINGS \n
			d - ROOT13 COM 2 LISTAS \n
			e - ROOT13 COM 2 STRINGS \n
			f - ROOT13 COM MAKETRNS \n
			g - CRIPTOGRAFAR UM ARQUIVO \n
		""").lower()

# De acordo com a escolha, chama uma função diferente
if executar == 'a':
	FuncoesCriptografia.criptografa_dicionario()
elif executar == 'b':
	FuncoesCriptografia.criptografa_lista()
elif executar == 'c':
	print FuncoesCriptografia.criptografa_strings()
elif executar == 'd':
	FuncoesCriptografia.criptografa_2_listas()
elif executar == 'e':
	FuncoesCriptografia.criptografa_2_strings()
elif executar == 'f':
	FuncoesCriptografia.criptografar_maketrans()
elif executar == 'g':
	FuncoesCriptografia.criptografa_arquivo()
else:
	print 'OPCAO NAO ENCONTRADA'




