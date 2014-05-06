#!/usr/bin/env python
# -*- coding: utf-8 -*-
# programa2.py - Exemplo de Endentação

def main():
    x = 1

    while True:
        print x,

        if x > 5:
            break
        else:
            print "menor"

        x += 1

    x = 0
    print "fim."

def nao_implementado():
    pass

if __name__ == '__main__': main() # evite fazer isso!
