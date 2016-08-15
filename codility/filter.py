# Filter just return True elements

n = [2,3,4,5,6,7,8,9,10]

print filter(lambda x : x if x % 2 == 0 else None, n)

# Using map:
[2, None, 4, None, 6, None, 8, None, 10]

# Using filter
[2, 4, 6, 8, 10]
