class dog(object):
        def __init__(self):
                print 'Object instaciate'

        def latir(self, ofthen):
                print 'Au! ' * ofthen

	def andar(self, steps = 2):
		print 'Seteps: ' * steps


class SaoBernardo(dog):
        def latir(self, ofthen = 1):
                super

	def andar(self, steps = 4):
		super(SaoBernardo, self).andar(steps = steps)

c = dog()
c.latir(1)

d = SaoBernardo()
d.latir(10)
d.andar(7)
