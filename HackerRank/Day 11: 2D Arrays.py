#!/bin/python3

# https://www.hackerrank.com/challenges/30-2d-arrays

import sys

'''
[[1, 1, 1, 0, 0, 0],
 [0, 1, 0, 0, 0, 0],
 [1, 1, 1, 0, 0, 0],
 [0, 0, 2, 4, 4, 0],
 [0, 0, 0, 2, 0, 0],
 [0, 0, 1, 2, 4, 0]]

 arr[i:3]
 [[1, 1, 1, 0, 0, 0],
  [0, 1, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 0]]
'''
arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]
# for arr_i in range(6):
#    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#    arr.append(arr_t)

def print_list(l):
   for i in l:
      print(str(i))

def get3x3(l, column):
   nl = []
   for i in l:
      nl.append(i[column:3:])

   return nl

count = 0
total = 0
max_count = 0
ct = []

for i in range(1,2):
   ct = (arr[i:i+3:])
   print_list(ct)
   print_list(get3x3(ct, i))

#
# for i in range(4): #Line
#     for j in range(4): # Column
#         for row in arr:
#             print(row[j:j+3:])
#             if count in [0, 2]:
#                 total += sum(row[j:j+3:])
#             elif count == 1:
#                 total += row[1]
#
#             count += 1 if count < 2 else 0
# else:
#   max_count = total if total > max_count else max_count
#   total = 0
#
# print(max_count)
