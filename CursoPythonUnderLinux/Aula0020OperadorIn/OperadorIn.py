#!/usr/bin/env python
#-*- coding:utf8 -*-

if 'teste' in 'Este é um teste':
	print 'A palavra \'teste\' esta contida na String \'Este é um teste\''
else:
	print 'A palavra \'teste\' não esta contida na String \'Este é um teste\''

if 'a' in ['q', 'w', 'a']:
	print "A letra 'a' está presente na lista"

if 'a' in ('q', 'w', 'a'):
        print "A letra 'a' está presente na tupla"

if 'a' in {1:'q', 2:'w', 'a':'3'}: #Neste caso do dicionário o in só busca dentro das chaves
        print "A letra 'a' está presente no dicionário" 


