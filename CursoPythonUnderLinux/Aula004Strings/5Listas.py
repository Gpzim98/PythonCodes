print 'As listas sao como as tuplas, porem mutaveis'

a = [1]
b = [a, 'asdf']

print 'Listas com unico elemento nao precisa de vilgura'
print a

print 'Listas com elementos de tipos diversos'
print b

print 'Uniao de listas'
print a + b

print 'Repeticao de listas'
print b * 3

c = ('Item 1 Tupla', 'Item 2 tupla')
d = ['Item 1 Lista', c]
print 'Listas com tuplas como item'
print d
