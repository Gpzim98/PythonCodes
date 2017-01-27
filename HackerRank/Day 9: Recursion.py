def factorial(n):
    if n == 1:
        # stoping condition...
        # we must stop when n is 1.
        return 1
    else:
        # recursion call...
        # multiply number by the previous factorial.
        return n * factorial(n-1)

print(factorial(int(input())))