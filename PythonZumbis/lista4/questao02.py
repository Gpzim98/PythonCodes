from random import randint

lista = [
    randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100), randint(1, 100),
    randint(1, 100), randint(1, 100)]

lista_impar = []
lista_par = []
i = 0

while i < 10:
    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])
    i += 1

print lista
print lista_impar
print lista_par
