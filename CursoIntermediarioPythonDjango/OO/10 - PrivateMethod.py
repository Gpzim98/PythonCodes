class Dog(object):
    __name = ''

    def public_method(self):
        print 'Public Method'

    def __private_method(self):
        print 'Private Method'


c = Dog()
c.public_method()
c._Dog__private_method
