class Dog(object):

    def __init__(self):
        print 'Object instaciate'

    def latir(self, ofthen):
        print 'Au! ' * ofthen

    def andar(self, steps=2):
        print 'Seteps: ' * steps


class SaoBernardo(Dog):
        pass

c = Dog()
c.latir(1)

d = SaoBernardo()
d.latir(10)
d.andar(7)
