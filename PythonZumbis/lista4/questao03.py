from random import randint

lista1 = [
    randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100)]

lista2 = [
    randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100)]

i = 0
lista3 = []
conta_lista1 = 0
conta_lista2 = 0

while i < 22:
    if i % 2 == 0:
        lista3.append(lista1[conta_lista1])
        conta_lista1 += 1
    else:
        lista3.append(lista2[conta_lista2])
        conta_lista2 += 1
    i += 1

print lista1
print lista2
print lista3
