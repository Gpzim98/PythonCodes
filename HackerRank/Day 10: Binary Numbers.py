#!/bin/python3
# https://www.hackerrank.com/challenges/30-binary-numbers
# bin(6)[2:].zfill(8)

import sys

# 64 32 16 8 4 2 1
# 0  1  1  1 1 1 1

n = int(input().strip())

bin8 = lambda x : ''.join(reversed([str((x >> i) & 1) for i in range(50)]))

num = bin8(n)

ant = ''

seq = 0

max = 0

for i in bin8(n):
    if (i == '1') and (ant == '1'):
        seq += 1
    else:
        max = seq if seq > max else max
        ant = i
        seq = 1 if i == '1' else 0
else:
    max = seq if seq > max else max

print(max)
