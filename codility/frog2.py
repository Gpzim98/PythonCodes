def solution(X, Y, D):
    if (X == Y) or (D == 0):
        return 0

    if ((Y-X)%D) !=0:
        return ((Y-X) / D) + 1
    else:
        return ((Y-X) / D)

print solution(0, 40, 3)
print solution(10, 85, 30)
print solution(10, 10, 30)
print solution(10, 11, 30)
print solution(0, 12, 3)