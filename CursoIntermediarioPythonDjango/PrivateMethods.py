class Dog(object):
	def __myPrivateMethod(self):
		print 'Private Method'
	
	def myPublicMethod(self):
		print 'My public Method'

print 'asdf'
myDog = Dog()
import pdb
pdb.set_trace()
print 'asdf'

