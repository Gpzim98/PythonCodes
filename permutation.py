#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(A):

    A.sort()

    for i in xrange(len(A)):
        if (i+1) != A[i]:
            return 0
    else:
        return 1


print(solution([1, 2, 3, 4]))
print(solution([1, 3, 4]))
print(solution([2,1,3,4,5,6,8,9,7]))
