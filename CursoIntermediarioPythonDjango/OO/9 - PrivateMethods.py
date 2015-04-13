class C(object):

    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        print 'Getter'
        return self._x

    @x.setter
    def x(self, value):
        print 'Setter'
        self._x = value

    @x.deleter
    def x(self):
        print 'Delete'
        del self._x

c = C()
c.x = 'Setando'
print c.x
del(c.x)
