x = 10

# It sucks
# def foo():
#     x += 11
#     print x


def foo():
    global x 
    x += 11
    print x

foo()