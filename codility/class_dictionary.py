class DefaultDict(dict):
  def __missing__(self, key):
    return []

d = DefaultDict()
d['florp'] = 127
d['florp'] = 127
print d

'''
Yes, it will work. With this implementation of the DefaultDict class, 
whenever a key is missing, the instance of the dictionary will 
automatically be instantiated with a list.
'''