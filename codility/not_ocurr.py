def solution(A):
    A.sort()

    cont = A[0]

    for i in A:
        if (1 <= i != cont) and (i != A[A.index(i)+1]):
            return cont
        else:
            cont+=1



print(solution([1, 3, 6, 4, 1, 2] ))
print(solution([1, 2, 3, 4]))
print(solution([0,1, 3, 4]))
print(solution([0,2,1,3,4,5,6,8,9,7]))
