def solution(X):
    excess = X % 20000 if X > 20000 else 0
    X = X if X < 20000 else 20000
    
    tax = (X * 0.2) + (excess * 0.4) - 3300
    
    return int(tax) if tax >= 0 else 0

print solution(18000)
print solution(30000)
print solution(0)
print solution(-1)
