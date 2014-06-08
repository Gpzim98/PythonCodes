#!/usr/bin/env python
# coding: utf-8

# Biblioteca do Python que criptografa em root13 (Foi usado apenas em um exemplo troca_extensao_arquivo)
import codecs
import string

# Classe Rot13 e a que tera todas as funcoes
class Rot13(object):

    # Funcao que abre o arquivo escolhido e criptografa
    def abre_arquivo_criptografa(self, caminho_arquivo, mostra_tela=True):
        
        # Try de seguranca caso o caminho do arquivo venha invalido
        try:
            # Abre o arquivo informado para leitura
            arq_origem = file(caminho_arquivo)
            # Abre o arquivo informado para escrita
            novo_arquivo = open(self.troca_extensao_arquivo(caminho_arquivo), "a")
        except IOError:
            # Caso o arquivo nao seja encontrado mostra esta mensagem
            print 'Arquivo nao encontrado!'
            return 0

        # Seta ponteiro de leitura no inicio do arquivo
        arq_origem.seek(0)
        # Loop para percorrer cada linha do arquivo a ser criptografado
        for linha in arq_origem:
            # Criptografa a linha atual usando a funcao encripata_dicionario e grava no arquivo
            novo_arquivo.write(self.encripta_dicionario(linha.strip()))
            novo_arquivo.write('\n')
        
        # No final, fecha os dois arquivos
        novo_arquivo.close()
        arq_origem.close()

        # Caso o usuario opte por mostrar os arquivos na tela este if executa
        if mostra_tela:
            arq_origem = file(caminho_arquivo)
            novo_arquivo = file(self.troca_extensao_arquivo(caminho_arquivo))
            print "*********ARQUIVO DE ORIGEM***********\n"
            for linha in arq_origem:
                print linha

            print "*********ARQUIVO DE DESTINO***********\n"
            for linha in novo_arquivo:
                print linha

    # Funcao para trocar a extensao do arquivo
    def troca_extensao_arquivo(self, caminho_arquivo):
        (prefix, sep, suffix) = caminho_arquivo.rpartition('.')
        return prefix + '.crp'
    
    #Encripta METODO 1
    # Metodo extra de uma biblioteca do Python para criptografar de forma facil com rot_13
    def encripta(self, texto):
        return codecs.encode(texto, 'rot_13')

    # Funcao que criptografa o texto buscando a letra (x+13) dentro de um dicionario
    def encripta_dicionario(self,texto):
        dictionary = {'a':'n', 'b':'o', 'c':'p','d':'q', 'e':'r', 'f':'s','g':'t','h':'u','i':'v','j':'w', 'k':'x','l':'y', 'm':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i', 'w':'j','x':'k','y':'l','z':'m'}
        rot13 = ''
        for c in texto:
            # Se a letra em questao for minuscula busca ela dentro do dicionario
            if c.islower():
                rot13 += dictionary.get(c)
            # Se a letra em questao for maiuscula busca ela dentro do dicionario e converte para MAIUSCULA
            if c.isupper():
                c = c.lower()
                rot13 += dictionary.get(c).capitalize()
            # Caso ela nao exista no dicionario, usa-se a propria letra, ex: letras com acento
            if c not in dictionary:
                rot13 += c
        return rot13

    # Funcao que criptografa o texto buscando a letra (x+13) dentro de uma lista
    def encripta_lista(self,texto):
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        c_alphabets = []
        
        # Criando uma outra lista com o alfabeto maiusculo
        for i in alphabets:
           c_alphabets.append(i.capitalize())

        resultado=''
        for i in texto:
            # Procuro a letra minuscula na lista, se nao achar busca ela na lista de letras MAIUSCULAS
            if i in alphabets:
                j = alphabets[(alphabets.index(i) + 13) % 26]
                resultado += j
            elif i in c_alphabets:
                j = c_alphabets[(c_alphabets.index(i) + 13) % 26]
                resultado += j
            # Se nao achar ela minus. nem maius. usa ela como esta. (Acentos e etc)
            else:
                resultado += i
        return resultado

    # Funcao que criptografa o texto buscando a letra (x+13) dentro de uma tupla
    # ATENCAO, AQUI FOI USADA A MESMA LOGICA DA LISTA, BASTA LER NELA QUE ESTARA ENTENDENDO NESTA
    def encripta_tupla(self,texto):
        alphabets = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        c_alphabets = ()

        for i in alphabets:
           c_alphabets = c_alphabets + (i.capitalize(),)
        resultado=''
        for i in texto:
            if i in alphabets:
                j = alphabets[(alphabets.index(i) + 13) % 26]
                resultado += j
            elif i in c_alphabets:
                j = c_alphabets[(c_alphabets.index(i) + 13) % 26]
                resultado += j
            else:
                resultado += i
        return resultado

    # Funcao que criptografa o texto buscando a letra (x+13) dentro de uma String
    def encripta_string(self,texto):
        chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        
        # Faz com que a variavel trans tenha o alfabeto com de N ate Z e A ate M ( Logica do Rot13)
        trans = chars[26:]+chars[:26]

        # Lambda cria a funcao rot_char que retorna a sentenca procurada na string trans se ela existir em chars
        rot_char = lambda c: trans[chars.find(c)] if chars.find(c) > -1 else c

        #De forma recursiva chama a funcao rot_char ate o fim da string (texto) passando cada caracter para ser convertido
        return ''.join(rot_char(c) for c in texto)

    # Funcao que criptografa o texto buscando de uma lista na outra lista na mesma posicao
    def encripta_com_2_listas(self, texto):
        # Aqui o alfabeto e partido em 2 listas
        alphabets_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
        alphabets_2 = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        resultado=''
        # Loop que percorre cada letra da string a ser convertida
        for i in texto:
            try:
                # Busca o indice (posicao) da letra procurada na lista 1
                indice = alphabets_1.index(i)
                # Se ela for encontrada eu guardo a letra correspondente neste mesmo indice so que pegando da lista 2
                resultado += alphabets_2[indice]                
            except ValueError:
                try:
                    # Busca o indice (posicao) da letra procurada na lista 1
                    indice = alphabets_2.index(i)
                    # Se ela for encontrada eu guardo a letra correspondente neste mesmo indice so que pegando da lista 1
                    resultado += alphabets_1[indice]                
                except ValueError:
                    # Caso a letra nao seja encontrada em nenhuma das listas, e usado o caracter original (por exemplo em caso de acnetos)
                    resultado += i
        return resultado

    # Funcao que criptografa o texto buscando de uma string na outra string na mesma posicao
    # ATENCAO, AQUI FOI USADA A MESMA LOGICA DA FUNCAO DE 2 LISTAS, BASTA LER NELA QUE ESTARA ENTENDENDO ESTA
    def encripta_com_2_strings(self, texto):
        alphabets_1 = "AaBbCcDdEeFfGgHhIiJjKkLlMm"
        alphabets_2 = "NnOoPpQqRrSsTtUuVvWwXxYyZz"

        resultado=''
        for i in texto:
            try:
                indice = alphabets_1.index(i)
                resultado += alphabets_2[indice]                
            except ValueError:
                try:
                    indice = alphabets_2.index(i)
                    resultado += alphabets_1[indice]                
                except ValueError:
                    resultado += i
        return resultado

    #Função Maketrans da biblioteca Strings do PYthon
    def encripta_maketrans(self, texto):
        # Conjunto dos caracteres do alfabeto sob a lógica do Rot13
        alfabeto = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
        # A função translate que faz a conversão 
        # recebe o que deve ser convertido também o nome da técnica a ser usado que neste caso é o rot_13
        print string.translate(texto, alfabeto)      
