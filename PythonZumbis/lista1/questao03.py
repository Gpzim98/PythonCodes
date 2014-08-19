dias = input('Digite os dias: ')
horas = input('Digite as horas: ')
minutos = input('Digite os minutos: ')
segundos = input('Digite os segundos: ')

total = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print(total)
