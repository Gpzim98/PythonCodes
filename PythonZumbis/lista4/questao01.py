from random import randint

lista = [
    randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100)]

maior = 0
menor = 999
i = 0

while i < 10:
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
    i += 1

print "Maior: %d, menor %d" % (maior, menor)
