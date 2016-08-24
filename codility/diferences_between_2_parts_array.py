import time 

def solution(a):
    p = len(a)

    lst = []

    j = xrange(1,p)
    print j

    for i in j:
        value = sum(a[:i:]) - sum(a[i::])
        lst.append(abs(value))

    return min(lst)

def solution2(A):
    top = A[0]
    rest = sum(A[1:])
    m = abs(top - rest)
 
    for index in xrange(1, len(A)-1):
        rest -= A[index]
        top += A[index]
        if abs(top-rest) < m:
            m = abs(top-rest)
 
    return m

# t = time.time()
# print solution(range(10000))
# print time.time() - t

t = time.time()
print solution2(range(10000))
print time.time() - t