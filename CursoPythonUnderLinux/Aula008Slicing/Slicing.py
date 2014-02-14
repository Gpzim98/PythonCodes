#-*- coding: utf-8 -*-
bandas = ["Rush", "The Cure", "Pink Floyd", "The Doors"]

myString = 'Curso de Python'

print '----------------------------------------------'
print 'Acessando o primeiro item: ', bandas[0]

print 'Acessando o último item: ', bandas[-1]

print 'Loop: ', bandas[0:2]

print 'Do segundo ate o último omitindo o último parâmetro:', bandas[1:]

print 'Do primeiro ate o quarto omitindo o primeiro parâmetro:', bandas[:3]

print 'Imprimindo tudo de tráz pra frente:', bandas[::-1]

print 'Do segundo item ao último de 2 em 2:', bandas[1::2]

print 'Do segundo ate o último omitindo o último parâmetro:', bandas[1:]

print 'Trabalhando com strings \n'

# A linha abaixo só pode acontecer com listas e dicionários pois 
# tuplas e strings não são mutáveis
bandas[0] = 'Banda Djavu'

print 'Adicionando um item em uma posição especifica da lista: ', bandas[::]

print 'Minha string completa com slicing:', myString[::]

print 'Minha string da terceira casa até o final:', myString[3:]

print 'Operações com strings: ', 'Este é o curso de' + myString[8:15]


print '----------------------------------------------'


