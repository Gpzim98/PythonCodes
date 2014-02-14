# -*- coding:utf8 -*-
idade = 25
nome  = 'Gregory'

print 'Olá, meu nome é %s e minha idade é %d' % (nome, idade)

print """Com vírgulas não é preciso converter, e os espaços são , 
colocados automáticamente: Minha idade é """, idade

print 'Com mais é precis converter: ' + str(idade) 

print """Programo em Python a %(chave2)d anos, 
e meu nome é %(chave1)s""" % {'chave1': 'Gregory Pacheco', 'chave2' : 2}

print """%(msg1)s %(msg1)s esse e um teste de %(msg2)s
""" % {'msg1':"Atencao!", 'msg2':'repeticao'}

ling = "Python"
dif  = "facil"
print "Eu estou aprendendo %(ling)s! Ela e muito %(dif)s!\n%(ling)s! %(ling)s! %(ling)s!" % vars()

print "Oi meu nome é %(chaveNome)s, eu sou um programador" % {'chaveNome' : 'Gregory Pacheco'}
