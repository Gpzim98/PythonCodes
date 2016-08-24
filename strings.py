print ("%d" % 10)
print ("%d %s %.2f" % (10, 'Gp', 1.2))
print ("{name} {age}".format(name='Gp', age=28))
print ("%s %d".format('Gp', 28)) # Doesn't work
lista = ['Gp', 28]
print ("{0} {1}".format(*lista))
dic = {'name': 'Gp', 'age': 28}
print ("{name} {age}".format(**dic))
nome = 'Gp'
idade = 28
print 'Ola, meu nome e %(nome)s, eu tenho %(idade)d anos.' % vars()
