anos = input('Anos que fuma:  ')
cig_dia = input('Cigarros por dia:  ')

minutos = int(cig_dia) * 10

minutos_perdidos = (int(anos) * 365) * minutos

print(str(minutos_perdidos))
