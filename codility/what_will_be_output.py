'''
What will be the output of the code below? Explain your answer.

How would you modify the definition of extendList to produce the presumably desired behavior?
'''
# O Python vai usar a mesma list criada anteriormente para chamadas que nao passam uma lista como parametro
# Por None no parametro da funcao resolve list = None
def extendList(val, list=[]):
  if list is None:
    list = []
  list.append(val)
  return list
  
list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print 'list1 = %s' % list1 # 10
print 'list2 = %s' % list2 # 123 
print 'list3 = %s' % list3 # a