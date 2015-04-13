class Dog(object):
    name = ''

    def set_dog_name(self, dog_name):
        self.name = dog_name

d = Dog()
d.set_dog_name('Rex')
print d.name
