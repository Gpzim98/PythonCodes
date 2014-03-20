class Dog(object):
	name = ''

def myFunction(dogName):
	c = Dog()
	c.name = dogName
	return c.name

print myFunction('Rex')
