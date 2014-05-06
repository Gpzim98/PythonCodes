class Cachorro(object):
	altura = 10
	def __init__(self):
		altura = 0

	def _get_altura(self):
		return self.altura
	def _set_altura(self, altura):
		self.altura = altura

	altura = property(_get_altura, _set_altura)

c = Cachorro()
c.altura = 20
#print c.altura
