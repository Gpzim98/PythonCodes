#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# grep1.py - Primeira versão do nosso utilitário de busca

import os
import sys

str_busca = sys.argv[1]
arquivos = sys.argv[2:]

for nome_arquivo in arquivos:
  arquivo = open(nome_arquivo)
  for numero_linha, linha in enumerate(arquivo):
    if str_busca in linha:
      dados = (nome_arquivo, numero_linha + 1, linha.strip(os.linesep))
      print "%s:%s: %s" % dados

