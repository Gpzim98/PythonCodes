class dog(object):
        def __init__(self):
                print 'Object instaciate'

        def latir(self, ofthen):
                print 'Au! ' * ofthen

class SaoBernardo(dog):
        def latir(self, ofthen = 1):
                print 'Woof! ' * ofthen

c = dog()
c.latir(1)

d = SaoBernardo()
d.latir(10)