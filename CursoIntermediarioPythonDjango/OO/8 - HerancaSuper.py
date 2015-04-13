class Dog(object):

    def __init__(self):
        print 'Object instaciate'

    def latir(self, ofthen):
        print 'Au! ' * ofthen

    def andar(self, steps):
        print 'Seteps: ' * steps


class SaoBernardo(Dog):

    def __init__(self):
        super(SaoBernardo, self).__init__()

    def latir(self, ofthen):
        super(SaoBernardo, self).latir(ofthen=ofthen)

    def andar(self, steps):
        super(SaoBernardo, self).andar(steps=steps)

c = Dog()
c.latir(5)
c.andar(5)

d = SaoBernardo()
d.latir(10)
d.andar(7)
