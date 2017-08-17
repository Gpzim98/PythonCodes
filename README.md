1 - ############ built-in zip function
for i, j in zip(list1, list2)

2 - ############ built-in enumerate function
for i,j in enumerate(lista)
    i = indice
    j = element

3 - ############ accessing a global variable
a = 10
def foo():
   global a
   a = 10

4 - ########### range performance
# Python 2.7
for i in range(100):
   # Bad Idea, range will be evaluate each loop iteration

a = range(100)
for i in a:
   # Good Idea
or

for i in xrange(100)
   # xrange is a Yield

# Python 3
range == xrange in Python 2.7

5 - ########## avoiding Dictionaries KeyError
dict.get(key, default)
instead of
dict[key]

6 - ########## for else
for i in xrange(10):
   pass
else: # Else means, no brak
   pass

7 - ########## try excepet else finally
# Python 2.7
try:
    pass
except Exception, e:
    raise
else: # Else means no exception
    pass
finally: # It will always execute
    pass

# Python 3
try:
 1/0
except (Exception, ZeroDivisionError) as e:
   print(e)
else:
   print('No exception')
finally:
   print('Finally')

8 - ########## List comprehension
m = [e for i in range(0, 10) for e in range(5) if ((e%2==0))]
m = [(i,e) for i in range(0, 10) for e in range(5) if ((e%2==0))]

9 - ########## String parameters Python
print ("%d" % 10)
print ("%d %s %.2f" % (10, 'Gp', 1.2))
print ("{name} {age}".format(name='Gp', age=28))
print ("%s %d".format('Gp', 28)) # Doesn't work
lista = ['Gp', 28]
print ("{0} {1}".format(*lista))
dic = {'name': 'Gp', 'age': 28}
print ("{name} {age}".format(**dic))
nome = 'Gp'
idade = 28
print('Ola, meu nome e %(nome)s, eu tenho %(idade)d anos.' % vars())


10 - ######### Args and kwargs Python
def f(args): # You use args when you don't know how many arguments might be passed
    print(type(args)) # list
    for i in args:
       print i

f([1,2,2])
t = (2,3,4,4)
f(t)
l = [3,3,3]
f(l)

# if you put * in the assinment parameters you should call the function puttin

def f2(**args):
    # **kwargs allows you to handle named arguments that you have not defined in advance
    print(type(args)) # print dict
    for name, value in args.iteritems():
        print name, value

f2(key1=10, key2=20)
f2({'g': 99, 'h':100}) # It doesn't work if you dont put **

11 - ######### Operations
Python 2.7

10/3 = 3
10//3. = 3.0 # Doble slashes forces round down

Python 3
10/3 = 3.3333333
10//3. = 3.0 # Doble slashes forces round down

12 - ######### Tuples vs Lists
Tuple, Imutable, less memory
Lists, Mutable, More memory

13 - ########## Named parameters
def f(a,b,c=10):
    print(a,b,c)

f(10,20,20)
f(10,20)
f(a=10, b=10)
f(a=10, c=10) # it doesn't work

14 - ########## Yeild
def primeiros(n):
    i = 0
    while i < n:
            yield i
            i += 1
    else:
            yield 'Fim'

for i in primeiros(10):
    print i

15 - ########## OO constructor
class Doc(object):
   def __init__:
      self.name = 'rex'

16 - ########## OO Inheritance
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

Object instaciate
Au!
Object instaciate
Woof! Woof! Woof! Woof! Woof! Woof! Woof! Woof! Woof! Woof!

17 - ########## OO Super
class SaoBernardo(dog):
        def latir(self, ofthen = 1):
                super(SaoBernardo, self).latir(ofthen=2)

18 - ########## OO accessing private atributes
myObj._ClassName__myPrivateMethod()

19 - ########## property/getter, setter, deleter
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
20 - ########## Iterators

21 - ########## Generators

22 - ########## Lambga
m = [lambda x  , i=i: (i * x) for i in range(3)]
x pararameter
i=i fixing i in each iteration
(i*x) return

23 - ########## Map
n = [2,4,6,8]
print map(lambda x: x**2, n)
[4, 16, 36, 64]

Python 3
l = ['1', '2']
l = list(map(int, l))

24 - ########## Reduce
n = [2,3,4,5,6]
print reduce(lambda x,  y : x + y, n)
# 20

25 - ########## Filter
# Filter just return True elements
n = [2,3,4,5,6,7,8,9,10]
print filter(lambda x : x if x % 2 == 0 else None, n)


26 - ########## Shallow copy and Deep Copy

27 - ########## input
input().strip()
Remove spaces from the begining and ending of string inputed

28 - ######## Threads
#!/usr/bin/python

import thread
import time

# Define a function for the thread
def print_time( threadName, delay):

   count = 0

   while count < 5:

      time.sleep(delay)

      count += 1

      print "%s: %s" % ( threadName, time.ctime(time.time()) )


# Create two threads as follows

try:

   thread.start_new_thread( print_time, ("Thread-1", 2, ) )

   thread.start_new_thread( print_time, ("Thread-2", 4, ) )

except:

   print "Error: unable to start thread"


while 1:

   pass

