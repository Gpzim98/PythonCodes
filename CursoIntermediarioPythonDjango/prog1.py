#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# prog1.py - Primeiro programa

import random

numero = random.randint(0, 100)

escolha = -1
tentativas = 0
while escolha != numero:
    escolha = input("Escolha um numero entre 0 e 100:")
    tentativas += 1
    if escolha < numero:
        print "O numero", escolha, "e menor que o sorteado."
    elif escolha > numero:
        print "O numero", escolha, "e maior que o sorteado."
print "Parabens! Voce acertou com", tentativas, "tentativas."
