#!/usr/bin/env python
import codecs


class Rot13(object):

    def abre_arquivo_criptografa(self, caminho_arquivo, mostra_tela=True):
        arq_origem = file(caminho_arquivo)
        novo_arquivo = open(self.troca_extensao_arquivo(caminho_arquivo), "a")
        # Seta ponteiro de leitura no inicio do arquivo
        arq_origem.seek(0)
        for linha in arq_origem:
            novo_arquivo.write(self.rot(linha.strip()))
            novo_arquivo.write('\n')
        novo_arquivo.close()
        arq_origem.close()

        if mostra_tela:
            arq_origem = file(caminho_arquivo)
            novo_arquivo = file(self.troca_extensao_arquivo(caminho_arquivo))
            print "*********ARQUIVO DE ORIGEM***********\n"
            for linha in arq_origem:
                print linha

            print "*********ARQUIVO DE DESTINO***********\n"
            for linha in novo_arquivo:
                print linha

    
    #Encripta METODO 1
    def encripta(self, texto):
        return codecs.encode(texto, 'rot_13')

    def encripta_dicionario(self,texto):
        dictionary = {'a':'n', 'b':'o', 'c':'p','d':'q', 'e':'r', 'f':'s','g':'t','h':'u','i':'v','j':'w', 'k':'x','l':'y', 'm':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i', 'w':'j','x':'k','y':'l','z':'m'}
        rot13 = ''
        for c in texto:
            if c.islower():
                rot13 += dictionary.get(c)
            if c.isupper():
                c = c.lower()
                rot13 += dictionary.get(c).capitalize()
            if c not in dictionary:
                rot13 += c
        return rot13

    def encripta_lista(self,texto):
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        c_alphabets = []
        
        for i in alphabets:
           c_alphabets.append(i.capitalize())
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

    def encripta_tupla(self,texto):
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        c_alphabets = []
        
        for i in alphabets:
           c_alphabets.append(i.capitalize())
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

    def encripta_string(self,texto):
        alphabets = 'abcdefghijklmnopqrstuvxz'
        c_alphabets = []
        
        for i in alphabets:
           c_alphabets.append(i.capitalize())
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

    def troca_extensao_arquivo(self, caminho_arquivo):
        (prefix, sep, suffix) = caminho_arquivo.rpartition('.')
        return prefix + '.crp'

# Descomente para testar no terminal
c = Rot13()
print 'Codecs: ' + c.encripta('hello')
print 'Dicionario: ' + c.encripta_dicionario('hello')
print 'Lista: ' + c.encripta_lista('hello')
print 'Tupla: ' + c.encripta_tupla('hello')
print 'String: ' + c.encripta_string('hello')
#c.abre_arquivo_criptografa('/home/gpzim98/Documentos/PythonCodes/Trabalhos/Rot13/arquivo_teste.txt', True)
