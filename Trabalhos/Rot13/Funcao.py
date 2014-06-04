#!/usr/bin/env python
import codecs


class Rot13(object):

    def abre_arquivo_criptografa(self, caminho_arquivo, mostra_tela=True):
        arq_origem = file(caminho_arquivo)
        novo_arquivo = open(self.troca_extensao_arquivo(caminho_arquivo), "a")
        # Seta ponteiro de leitura no inicio do arquivo
        arq_origem.seek(0)
        for linha in arq_origem:
            novo_arquivo.write(self.encripta(linha.strip()))
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

    def encripta(self, texto):
        return codecs.encode(texto, 'rot_13')

    def troca_extensao_arquivo(self, caminho_arquivo):
        (prefix, sep, suffix) = caminho_arquivo.rpartition('.')
        return prefix + '.crp'

# Descomente para testar no terminal
#c = Rot13()
#c.abre_arquivo_criptografa('/home/gpzim98/Documentos/Rot13/arquivo_teste.txt', True)
