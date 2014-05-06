def l():
    x = "L"
    print "l:", x # l(): L

def g():
    global x
    x = "G"
    print "g():", x # g(): G

x = "X"
print "X1:", x # X1: X
l()            # l(): L
print "X2:", x # X2: X
g()            # g(): G
print "X3:", x # X3: G
