def solution(S, P, Q):
    dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    lista = []

    for p, q in zip(P, Q):
        less = 7
        for i in xrange(p, q+1):
            if dict[S[i]] < less:
                less = dict[S[i]]
        else:
            lista.append(less)
    else:
        return lista


print solution('CAGGCTA', [2,5,0], [4,5,6])