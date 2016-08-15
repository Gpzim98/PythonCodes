def multipliers():
  # return [lambda x  : (i * x) for i in range(3)]

  # Solution
  return [lambda x  , i=i: (i * x) for i in range(3)]
    
print [m(4) for m in multipliers()]

# [8, 8, 8]
''' quando o for do print executa ele retorna um m iterable por que multipliers retona varias vezes  
    a definicao de uma funcao lamba. Logo, m e um iterable de funcoes. 
    O range faz devolver 3 funcoes, quando a funcao e retornada, ela sai da "fabrica" com i valendo 2
    com isso os numeros passados para M serao multiplicados por 2 
'''


# solving the problem
# a = lambda x,i : x * i 
# print [a(4,i) for i in range(3)]

'''
Other ways to solve this problem

def multipliers():
  for i in range(4): yield lambda x : i * x 

Another solution is to create a closure that binds immediately to its arguments by using a default argument. For example:

def multipliers():
  return [lambda x, i=i : i * x for i in range(4)]

Or alternatively, you can use the functools.partial function:

from functools import partial
from operator import mul

def multipliers():
  return [partial(mul, i) for i in range(4)]

'''