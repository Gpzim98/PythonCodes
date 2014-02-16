#!/usr/bin/env python
#-*- coding:utf8 -*-
a = 0
while a < 10:
   a += 1
   if a == 5:
      print 'Não imprime o 5'
      continue
   print 'Loop em: %d' % a
else:
   print 'Fim do programa'
