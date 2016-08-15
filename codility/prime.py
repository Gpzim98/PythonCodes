q = input()
a,b = raw_input().split(' ')

def is_prime(a):
    return all(a % i for i in xrange(2, a))

print 1    

for i in range(2, q):
    for j in range(int(a), int(b)):
        if is_prime(j):
            print j