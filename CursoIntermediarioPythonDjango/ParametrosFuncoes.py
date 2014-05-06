def func(a,b=10):
	return a + b

dic = {'a':50, 'b':50}
print func(**dic)

lista = [50,70]
print func(*lista)

tupla = (80,30)
print func(*tupla)

def soma(*args):
	a = sum(args)
	print 'Args na assinatura',a

soma(2,3)

print "Argumentos em strings - Nome: {nome} - Idade: {idade}".format(nome='gpzim', idade=25)

dic = {'nome':'Gp', 'idade':25}

print "Argumentos em strings - Nome: {nome} - Idade: {idade}".format(**dic)
