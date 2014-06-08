#!/usr/bin/env python
# coding: utf-8
import algoritimos

# Monta o menu que será mostrado ao usuário
# Na variavel escolha é colocada a opção escolhida
escolha  = input("""
			1 - CRIPTOGRAFAR USANDO DICIONARIO \n
			2 - CRIPTOGRAFAR USANDO LISTA \n
			3 - CRIPTOGRAFAR USANDO STRINGS \n
			4 - CRIPTOGRAFAR USANDO 2 LISTAS \n
			5 - CRIPTOGRAFAR USANDO 2 STRINGS \n
			6 - CRIPTOGRAFAR TULIZANDO A FUNCAO MAKETRNS \n
			7 - CRIPTOGRAFAR UM ARQUIVO \n
		""")

# De acordo com a escolha, chama uma função diferente
if escolha == 1:
	print 'VOCE ESTA USANDO A CRIPTOGRAFIA ROT13 COM DICIONARIOS\n'
	print algoritimos.root13_dicionario(raw_input('Digite algo para ser criptografado: '))
elif escolha == 2:
	print 'VOCE ESTA USANDO A CRIPTOGRAFIA ROT13 COM LISTA'
	print algoritimos.rot13_lista(raw_input('Digite algo para ser criptografado: '))
elif escolha == 3:
	print 'VOCE ESTA USANDO A CRIPTOGRAFIA ROT13 COM STRINS\n'
	print algoritimos.root13_string(raw_input('Digite algo para ser criptografado: '))
elif escolha == 4:
	print 'VOCE ESTA USANDO A CRIPTOGRAFIA ROT13 COM 2 LISTAS\n'
	print algoritimos.root13_com_2_listas(raw_input('Digite algo para ser criptografado: '))
elif escolha == 5:
	print 'VOCE ESTA USANDO A CRIPTOGRAFIA ROT13 COM 2 STRINGS\n'
	print algoritimos.root13_com_2_strings(raw_input('Digite algo para ser criptografado: '))
elif escolha == 6:
	print 'VOCE ESTA USANDO A CRIPTOGRAFIA ROT13 COM A FUNÇÃO MAKETRANS\n'
	print algoritimos.root13_com_maketrans(raw_input('Digite algo para ser criptografado: '))
elif escolha == 7:
	print 'VOCE ESTA USANDO A CRIPTOGRAFIA ROT13 COM A FUNÇÃO MAKE TRANS\n'
	mostrar = raw_input("Digite SIM para mostrar o arquivo criptografado na tela: ").lower()
	algoritimos.root13_arquivo(raw_input('Informe o caminho do arquivo a ser criptografado: '), mostrar == 'sim')
else:
	print 'OPCAO NAO ENCONTRADA'

