class C(object):
    def __init__(self):
        self._x = None

    @property
    def getX(self):
        print 'Getter'
        return self._x

    @getX.setter
    def setX(self, value):
        print 'Setter'
        self._x = value

    @getX.deleter
    def delX(self):
        print 'Delete'
        del self._x

c = C()
c.setX = 'Setando'
print c.getX
del(c.delX)