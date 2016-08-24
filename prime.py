def prime(n):
    lista = []

    for j in n:
        if j > 1:
            for i in xrange(2, j):
                if j % i == 0:
                    break
            else:
                lista.append(j)

    return lista

print(prime([2, 3, 5, 8, 13 ]))
