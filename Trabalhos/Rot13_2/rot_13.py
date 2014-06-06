#!/usr/bin/env python
import algoritimos

escolha  = input("""
			1 - CRIPTOGRAFAR USANDO DICIONARIO \n
			2 - CRIPTOGRAFAR USANDO LISTA \n
			3 - CRIPTOGRAFAR USANDO STRINGS \n
			4 - CRIPTOGRAFAR USANDO 2 LISTAS \n
		""")

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

else:
	print 'OPCAO NAO ENCONTRADA'

