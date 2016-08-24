def solution(A):
    pairs = 0
    east = 0
    for i in xrange(len(A)):
        if A[i] == 0:
            east += 1

            if pairs > 1000000000:
                return -1
        else:
            pairs += east

    return pairs

print(solution([0, 1, 0, 1, 1]))
