peso = input("Peso: ")

peso_exced = 0

if peso > 50:
    peso_exced = peso - 50
multa = peso_exced * 4

print "Peso excedente: " + str(peso_exced)
print "Multa: ", multa
