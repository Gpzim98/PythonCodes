n = range(0,20)
n = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]

# m = [e for i in range(0, len(n)) for e in n if ((e%2==0) and (n.index(e) % 2 == 0))]

m = [e for e in n[::2] if e % 2 == 0]

print n
print m