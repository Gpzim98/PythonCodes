#!/usr/bin/env python
# coding: utf-8
import os

def root13_dicionario(converter):
        retorno = ''
        alfabeto = {'a':'n', 'b':'o', 'c':'p','d':'q', 'e':'r', 'f':'s','g':'t','h':'u','i':'v','j':'w', 'k':'x','l':'y', 'm':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i', 'w':'j','x':'k','y':'l','z':'m'}

        #Loop que percorre cada letra do parametro (converter) e acha a letra 13 posições a frente
        for letra in converter:
            # Verifica se é minuscula
            if letra in alfabeto or letra.lower() in alfabeto:
                if letra.islower():
                    retorno += alfabeto.get(letra)
                # Verifica se é maiuscula
                elif letra.isupper():
                    letra = letra.lower()
                    retorno += alfabeto.get(letra).capitalize()
            # Caso a letra não esteja no dicionário usa-a como esta. Por exemplo quando possui acentos
            else:
                retorno += letra
        return retorno

def rot13_lista(converter):
    retorno=''
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    #Loop que percorre cada letra do parametro (converter) e acha a letra 13 posições a frente
    for letra in converter:
        # Verifica se ela esta no alfabeto, seja maiuscula ou minuscula
        if letra in alfabeto or letra.lower() in alfabeto:
            j = alfabeto[(alfabeto.index(letra.lower()) + 13) % 26]
            # Se ela for minuscula, passa-a desta forma
            if letra.islower():
                retorno += j
            else:
                # Caso não seja minuscula passa-a maiuscula
                retorno += j.upper()
        # Caso a letra não esteja no dicionário usa-a como esta. Por exemplo quando possui acentos
        else:
            retorno += letra
    return retorno

def root13_string(converter):
    alfabeto_minusculo = ''.join(chr(c) for c in range (97,123)) # Monta o alfabeto minusculo
    alfabeto_maiusculo = ''.join(chr(c) for c in range (65,91)) #Monta o alfabeto maiusculo
    minusculo_encode = alfabeto_minusculo[13:] + alfabeto_minusculo[:13] #Monta o alfabeto com as posições trocadas de acordo com o Rot13
    maiusculo_encode = alfabeto_maiusculo[13:] + alfabeto_maiusculo[:13] #Monta o alfabeto com as posições trocadas de acordo com o Rot13
    output = "" #Variavel com o retorno
    
    #Loop que percorre cada letra do parametro (converter) e acha a letra 13 posições a frente
    for c in converter:
        # Procura o caractere no alfabeto minusculo
        if c in alfabeto_minusculo:
                output = output + minusculo_encode[alfabeto_minusculo.find(c)]
        # Procura o caractere no alfabeto maiusculo
        elif c in alfabeto_maiusculo:
            output = output + maiusculo_encode[alfabeto_maiusculo.find(c)]
        # Caso a letra não esteja no dicionário usa-a como esta. Por exemplo quando possui acentos
        else:
            output = output + c
    return output

def root13_com_2_listas(converter):
        converter = converter.lower()
        retorno=''
        alfabeto_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
        alfabeto_2 = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        #Loop que percorre cada letra do parametro (converter) e acha a letra 13 posições a frente
        for letra in converter:
            # Tenta achar a letra dentro da primeira metade do alfabeto
            try:
                retorno += alfabeto_2[alfabeto_1.index(letra)]                
            except ValueError:
                # Tenta achar a letra dentro da primeira metade do alfabeto
                try:
                    retorno += alfabeto_1[alfabeto_2.index(letra)]                
                # Caso não encontre em nenhum deles, usa o caractere original como em casos de acentos
                except ValueError:
                    retorno += letra
        return retorno    

def root13_com_2_strings(converter):
        alfabeto_1 = "AaBbCcDdEeFfGgHhIiJjKkLlMm"
        alfabeto_2 = "NnOoPpQqRrSsTtUuVvWwXxYyZz"

        resultado=''
        #Loop que percorre cada letra do parametro (converter) e acha a letra 13 posições a frente
        for letra in converter:
            # Veririca se a letra esta na string
            if alfabeto_1.rfind(letra) != -1:
                # Captura a posição dela na string
                posicao = alfabeto_1.index(letra)
                # Busca a letra daquela posição e guarda na variável regorno
                resultado += alfabeto_2[posicao]                
            # Verifica se a letra esta na outra string
            elif alfabeto_2.rfind(letra) != -1:      
                # Captura a posição dela na string      
                posicao = alfabeto_2.index(letra)
                # Busca a letra daquela posição e guarda na variável regorno
                resultado += alfabeto_1[posicao]                
            # Caso não encontre em nenhum deles, usa o caractere original como em casos de acentos
            else:            
                resultado += letra
        return resultado       

#Função Maketrans da biblioteca Strings do PYthon
def root13_com_maketrans(converter):
    import string
    # Conjunto dos caracteres do alfabeto sob a lógica do Rot13
    rot13 = string.maketrans( 
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    # Chamada da função translate que faz a conversão 
    # recebendo o que deve ser convertido e o algoritimo a ser usado que neste caso é o rot_13
    return string.translate(converter, rot13)        

# Função que codifica um arquivo de texto
def  root13_arquivo( caminho, exibir_na_tela=True):
    # Verifica se o caminho passado é de um arquivo de verdade
    if os.path.isfile(caminho):
        # Caso ele exista, abre-o para leitura
        arquivo_1 = file(caminho)
    else:
        print 'Arquivo não encontrado'
        return 0
    
    # Cria o novo arquivo para escrita do texto já codificado
    # Aqui o arquivo já é criado realizando a troca da extensão com a funcção muda_extensao_arquivo
    arquivo_2 = open(muda_extensao_arquivo(caminho), "a")
    # Seta o arquivo na primeira linha
    arquivo_1.seek(0)
    # Loop que percorre o arquivo linha por linha
    for linha in arquivo_1:
        # Escreve no novo arquivo já encriptando com o rot_13
        arquivo_2.write(root13_com_2_strings(linha.strip()) + '\n')
        # Caso o usuário tenha optado por imprimir na tela, este if é executado
        if exibir_na_tela and linha.strip() != None:
            print root13_com_2_strings(linha.strip()) + '\n'
            
    # Fecha os dois arquivos abertos
    arquivo_2.close()
    arquivo_1.close()

# Função que altera a extensão do arquivo
def muda_extensao_arquivo(caminho):
    # Percorre o nome do arquivo ate achar um ponto, 
    # dai ele parte o nome do arquivo para saber qual é a extensão (sufixo)
    (prefix, sep, suffix) = caminho.rpartition('.')
    return prefix + '.crp'      