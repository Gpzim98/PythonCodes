# -*- coding:utf-8 -*-

def solution(A):
    ''' Solve it with Pigeonhole principle.
        There are N integers in the input. So for the
        first N+1 positive integers, at least one of
        them must be missing.
    '''
    # We only care about the first N+1 positive integers.
    # occurrence[i] is for the integer i+1.
    occurrence = [False] * (len(A) + 1)
    for item in A:
        if 1 <= item <= len(A) + 1:
            occurrence[item - 1] = True

    # Find out the missing minimal positive integer.
    for index in xrange(len(A) + 1):
        if occurrence[index] == False:
            return index + 1

    raise Exception("Should never be here.")
    return -1


assert solution([-1]) == 1
assert solution([1, 3, 6, 4, 1, 2]) == 5
assert solution([1]) == 2
assert solution([-1, 0, 1, 3]) == 2
assert solution([-1, 0, 1, 2]) == 3