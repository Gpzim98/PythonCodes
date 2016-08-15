def solution(a, K):
    return a.index(K) if a.count(K) else -1

a = [1,3,1,4,2,3,5,4]
print solution(a, 5)