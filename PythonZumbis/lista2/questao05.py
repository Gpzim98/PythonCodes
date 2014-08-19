n1 = input("Numero 1: ")
n2 = input("Numero 2: ")
n3 = input("Numero 3: ")

if n1 > n2 > n3:
    if n2 > n3:
        print "Maior: %d menor %d" % (n1, n3)
    else:
        print "Maior: %d menor %d" % (n1, n2)
if n2 > n1 > n3:
    if n1 > n3:
        print "Maior: %d menor %d" % (n2, n3)
    else:
        print "Maior: %d menor %d" % (n2, n1)
if n3 > n2 > n1:
    if n2 > n1:
        print "Maior: %d menor %d" % (n3, n1)
    else:
        print "Maior: %d menor %d" % (n3, n2)
