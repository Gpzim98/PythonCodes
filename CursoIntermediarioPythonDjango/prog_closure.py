# -*- encoding: utf-8 -*-

def fib(n):
    if n < 2: return 1
    return fib(n-1) + fib(n-2)

def memoize(fn):
    memo = {}
    def memoizer(*param1):
        key = repr(param1)
        if not key in memo:
            memo[key] = fn(*param1)
        return memo[key]
    return memoizer

import time

t1 = time.time()
for x in range(5):
    fib(35)
t2 = time.time()

print "Tempo médio em 5 execuções (sem memo):", round((t2-t1)/5,4)

fib = memoize(fib)

t1 = time.time()
for x in range(5):
    fib(35) # muuuito mais lento
t2 = time.time()
print "Tempo médio em 5 execuções (com memo):", round((t2-t1)/5,4)


def memoize(fn):
    memo = {}
    def memoizer(*param1):
        key = repr(param1)
        if not key in memo:
            memo[key] = fn(*param1)
        return memo[key]
    return memoizer

@memoize
def fib(n):
    if n < 2: return 1
    return fib(n-1) + fib(n-2)
