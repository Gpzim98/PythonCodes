def solution(N):
    seq = 0
    a = str(bin(N))
    b = a.split('1')[1::]
    b.sort()
    return len(b[-1])
    
print solution(1041)