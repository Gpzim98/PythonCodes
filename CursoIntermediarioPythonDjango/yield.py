def myYield(cont):
	while cont > 0:
		yield cont
		cont-=1
	else:
		yield 'Fim'

def testaYield(cont):
	for i in myYield(cont):
		print i


testaYield(50)
