#!/usr/bin/env python
#-*- coding:utf8 -*-

n1 = float(raw_input("Por favor digite o primeiro numero: "))
n2 = float(raw_input("Por favor digite o segundo numero: "))
 
resultado = 'O denominador não pode ser zero!' if n2 == 0 else 'Resultado: '+str(n1/n2)
 
print resultado
