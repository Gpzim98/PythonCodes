n = 14


def main():
    n = 188
    def is_prime(n):
        prime = False
        for i in xrange(2, n):
            if n % i == 0:
                prime = False
                break
        else:
            prime = True
        return prime

    if is_prime(n):
        return 1
    high = 0
    for i in xrange(2, n):
        if (n % i == 0) and (is_prime(i)):
            high = i
    else:
        return high
print main()