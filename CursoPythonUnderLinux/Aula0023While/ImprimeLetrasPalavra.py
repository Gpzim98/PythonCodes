#!/usr/bin/env python
#-*- coding:utf8 -*-

palavra = raw_input('Digite uma palavra:')
palavra = palavra[::-1]
size = len(palavra)
while size > 0:
    size -= 1
    print palavra[size]
