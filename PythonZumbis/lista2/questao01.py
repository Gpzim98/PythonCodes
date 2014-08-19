a = input("Lado 1: ")
b = input("Lado 2: ")
c = input("Lado 3: ")

if a > b + c or b > c + a or c > a + b:
    print "Nao e um triangulo"
elif a != b != c:
    print "Escaleno"
elif a == b == c:
    print "Equilatero"
else:
    print "Isoceles"
