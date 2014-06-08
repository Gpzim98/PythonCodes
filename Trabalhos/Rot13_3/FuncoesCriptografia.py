#!/usr/bin/env python
# coding: utf-8

def criptografa_dicionario():
    retorno = ''

    print 'VOCE ESTA USANDO A CRIPTOGRAFIA ROT13 COM DICIONARIOS\n'
    
    string = raw_input('Degite a frase de para ser traduzida para o rot13: ')

    alfabeto = {'a':'n', 'b':'o', 'c':'p','d':'q', 'e':'r', 'f':'s','g':'t','h':'u','i':'v','j':'w', 'k':'x','l':'y', 'm':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i', 'w':'j','x':'k','y':'l','z':'m',
    	           'A':'N', 'B':'O', 'C':'P','D':'Q', 'E':'R', 'F':'S','G':'T','H':'U','I':'V','J':'W', 'K':'X','L':'Y', 'M':'Z','N':'A','O':'B','P':'C','Q':'D','R':'E','S':'F','T':'G','U':'H','V':'I', 'W':'J','X':'K','Y':'L','Z':'M'}

    #Loop que percorre cada letra da string e acha a letra 13 posições a frente
    for letra in string:
        # Verifica se a letra em questão faz parte do alfabeto
        if letra in alfabeto:
        	#Concatena letra por letra no retorno
                retorno += alfabeto.get(letra)
         # Caso a letra não esteja no dicionário usa-a como esta. Por exemplo quando possui acentos
        else:
            retorno += letra
    print retorno

def criptografa_lista():
    retorno = ''

    print 'VOCE ESTA USANDO A CRIPTOGRAFIA ROT13 COM LISTA\n'
    
    string = raw_input('Degite a frase de para ser traduzida para o rot13: ')
    
    alf_minusc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alf_maiusc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    #Loop que percorre cada letra da string e acha a letra 13 posições a frente
    for letra in string:
    	#Verifica se a letra existe na lista de letras minusculas
        if letra in alf_minusc:
            retorno+=alf_minusc[alf_minusc.index(letra)+13]
        #Verifica se a letra existe na lista de letras maiusculas
        elif letra in alf_maiusc:
            retorno+=alf_maiusc[alf_maiusc.index(letra)+13]   
        # Caso a letra não esteja no dicionário usa-a como esta. Por exemplo quando possui acentos
        else:
            retorno+=letra
    print retorno

def criptografa_strings():
	retorno = ''

	print 'VOCE ESTA USANDO A CRIPTOGRAFIA ROT13 COM STRINGS\n'
    
	string = raw_input('Degite a frase de para ser traduzida para o rot13: ')

	alfabeto = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

	# Faz com que a variavel caracteres_transpostos tenha o alfabeto de N ate Z e A ate M ( Logica do Rot13)
	caracteres_transpostos = alfabeto[26:]+alfabeto[:26]

	# Função que busca a letra passada (caracter) na string alfabeto, caso não encontre retorna a propria letra (caracter)
	def acha_letra_correspondente(caracter):
		if alfabeto.find(caracter) > -1:
			# Acha a letra correspondente em caracteres_transpostos de acordo com a posição dela na string alfabeto
			return caracteres_transpostos[alfabeto.find(caracter)] 
		else: 
		 	return caracter
	
	#Para cada letra da string chama a função acha_letra_correspondente e traduz ela para a letra correspondente no rot13
	return ''.join(acha_letra_correspondente(letra) for letra in string)    

def criptografa_2_listas():
	# Aqui o alfabeto e partido em 2 listas
	alfa1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
	alfa2 = ['n','o','p','q','r','s','t','u','v','w','x','y','z']

	retorno = ''

	print 'VOCE ESTA USANDO A CRIPTOGRAFIA ROT13 COM 2 LISTAS\n'
    
	string = raw_input('Degite a frase de para ser traduzida para o rot13: ')

	#Loop que percorre cada letra da string e acha a letra 13 posições a frente
	for letra in string:
		try:
			# Captura a posição da letra no alfabeto1
			indice = alfa1.index(letra.lower())
			# Guarda na variavel retorno a letra minuscula caso ela seja minuscula, se não converte ela para maiuscula (upper())
			retorno += alfa2[indice] if letra.islower() else alfa2[indice].upper()
		except Exception, e:
			try:
				# Captura a posição da letra no alfabeto2
				indice = alfa2.index(letra.lower())
				# Guarda na variavel retorno a letra minuscula caso ela seja minuscula, se não converte ela para maiuscula (upper())
				retorno += alfa1[indice] if letra.islower() else alfa1[indice].upper()
			except Exception, e:
				# Retorna a letra original caso ela não tenha sido encontrada em nenhuma das listas, em caso de caracteres com acento
				retorno += letra
	print retorno

def criptografa_2_strings(string=None):	
	retorno = ''

	# Caso nada tenha sido passado como parametro na chamada da função, 
	# É pedido para o usuário digigar o que ele quer que seja criptografado
	if string is None:
		print 'VOCE ESTA USANDO A CRIPTOGRAFIA ROT13 COM 2 STRINGS\n'
    		string = raw_input('Degite a frase de para ser traduzida para o rot13: ')
    		# A variavel flag é setada como false, para saber que a funçao foi chamada sem passar uma string
    		# Ou seja, a string esta sendo recebida aqui dentro
    		flag = False
    	else:
    		# Caso a função tenha sido chamada passando já a string, flag recebe True, 
    		# pois assim não vamos imprimir a frase criptografada aqui dentro
    		flag = True

	alfa1 = "AaBbCcDdEeFfGgHhIiJjKkLlMm"
	alfa2 = "NnOoPpQqRrSsTtUuVvWwXxYyZz"

	resultado=''
	#Loop que percorre cada letra da string e acha a letra 13 posições a frente
	for letra in string:
		try:
			# Acha a posição da letra no alfabeto original
			indice = alfa1.index(letra)
			# Busca a letra desta mesma posição mas na outra string
			retorno += alfa2[indice]                
		except Exception, e:
			try:
				# Acha a posição da letra no alfabeto original, e busca a correspondente na outra string
				retorno += alfa1[alfa2.index(letra)]                
			except Exception, e:
				# Retorna a letra original caso ela não tenha sido encontrada em nenhuma das listas, em caso de caracteres com acento
				retorno += letra
	# Se flag foi setada como true no início da função vamos apenas retornar a variavel, se não vamos imprimi-la aqui mesmo
	if flag:
		return retorno
	else:
		print retorno

#Função Maketrans da biblioteca Strings do PYthon
def criptografar_maketrans():
	import string
	print 'VOCE ESTA USANDO A CRIPTOGRAFIA ROT13 COM 2 STRINGS\n'

	string_conv = raw_input('Degite a frase de para ser traduzida para o rot13: ')

	# Conjunto dos caracteres do alfabeto sob a lógica do Rot13
	alfabeto = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
		"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	# A função translate que faz a conversão 
	# recebe o que deve ser convertido também o nome da técnica a ser usado que neste caso é o rot_13
	print string.translate(string_conv, alfabeto)       	

def  criptografa_arquivo():
	import os

	print 'VOCE ESTA USANDO A CRIPTOGRAFIA DE ARQUIVOS\n'
	caminho_arquivo = raw_input('Informe o caminho do arquivo: ')
	imprime_arquivo = raw_input('Deseja visualizar o arquivo criptografado na tela? Digite Sim ou Não: ').lower()
	
	# Checa se o arquivo informado pelo usuário existe
	if os.path.isfile(caminho_arquivo):
		# Caso exista, abre-o para leitura
		orig = file(caminho_arquivo)
	else:
		print 'Arquivo não encontrado'
		return 0

	# Cria um arquivo correspondente com a extensão alterada para .crp
	dest = open(altera_extensao_arquivo(caminho_arquivo), "a")
	
	# Faz com que a leitura do arquivo original seja a partir da primeira linha (0)
	orig.seek(0)
	
	# Loop que percorre todas as linhas do arquivo
	for linha in orig:
		# Escreve cada linha do arquivo original no arquivo .crp já criptografando, chamando a função criptografa_2_strings
		dest.write(criptografa_2_strings(linha.strip()) + '\n')
	
		# Se o usuário optou por imprimir o resultado na tela, este if é executado
		if imprime_arquivo and linha.strip() != None:
			print criptografa_2_strings(linha.strip()) + '\n'

	# Ao final fecha-se os 2 arquivos
	dest.close()
	orig.close()

# Função que altera a extensão do arquivo
def altera_extensao_arquivo(caminho_arquivo):
    # Percorre o nome do arquivo ate achar um ponto, 
    # dai ele parte o nome do arquivo para saber qual é a extensão (sufixo)
    (prefix, sep, suffix) = caminho_arquivo.rpartition('.')
    return prefix + '.crp'      	