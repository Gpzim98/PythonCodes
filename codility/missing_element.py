# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    A.sort()
    for i in A:
        if A[i] != i+1:
            return i+1