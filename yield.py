def primeiros(n):
    i = 0
    while i < n:
            yield i
            i += 1
    else:
            yield 'Fim'

for i in primeiros(10):
    print i
