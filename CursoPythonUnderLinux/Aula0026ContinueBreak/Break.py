#!/usr/bin/env python
#-*- coding:utf8 -*-
a = 0
while a < 10:
   a += 1
   if a == 5:
      print 'Hora de parar'
      break
   print 'Loop em: %d' % a
else:
   print 'Fim do programa'
