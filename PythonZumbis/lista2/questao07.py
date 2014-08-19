area_pintar = input("Tamanho da area a ser pintada: ")

litros = area_pintar / 3.0

if (litros / 18) > 0:
    latas = int((litros / 18) + 1)
else:
    latas = int((litros / 18))

print "Total de latas necessarias: ", latas
