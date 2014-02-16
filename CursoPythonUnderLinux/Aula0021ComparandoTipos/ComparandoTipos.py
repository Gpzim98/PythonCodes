#!/bin/usr/env python
#-*- coding:utf8 -*-

var = input("Informe uma variavel para ser analisada: ")
tipo = type(var)
if tipo == int:
    print 'Você infomrou um numero inteiro.'
elif tipo == float:
    print 'Você infomrou um numero ponto flutuante.'
elif tipo == str:
    print 'Você infomrou uma string.'
elif tipo == dict:
    print 'Você infomrou um dicionario.'
elif tipo == list:
    print 'Você infomrou uma lista.'
elif tipo == tuple:
    print 'Você infomrou uma tupla.'
else:
    print 'Desconheço esse tipo de variável.'
