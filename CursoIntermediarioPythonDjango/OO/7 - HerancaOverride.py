class Dog(object):

    def __init__(self):
        print 'Object instaciate'

    def latir(self, ofthen):
        print 'Au! ' * ofthen

    def andar(self, steps):
        print 'Seteps: ' * steps


class SaoBernardo(Dog):

    def __init__(self):
        print 'Um Sao Bernardo intanciado'

    def latir(self, ofthen):
        print 'Wof ' * ofthen

    def andar(self, steps):
        print 'Clop ' * steps

c = Dog()
c.latir(5)
c.andar(5)


d = SaoBernardo()
d.latir(10)
d.andar(7)
