def solution(A, K):
    tmp1 = 0
    for i in range(K):
        b = A[:-1:]
        b.insert(0,A[-1])
        A = b
    return A
    
A = [3, 8, 9, 7, 6]    
print solution(A, 3)