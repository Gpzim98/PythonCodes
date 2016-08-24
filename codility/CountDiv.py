def solution(A, B, K):
    edge = 1 if A%K == 0 else 0
    return B//K - A//K + edge

print solution(10,10,5)
