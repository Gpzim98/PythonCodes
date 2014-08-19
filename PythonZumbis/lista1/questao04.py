salario = input('Digite o salario: ')
per_aum = input('Digite o percentual de aumento (Ex.: 0.10 = 10%): ')

salario = float(salario)
per_aum = float(per_aum)

novo_salario = salario + (salario * per_aum)
aumento = (salario * per_aum)

print("Valor do novo salario: " + str(novo_salario))
print("Aumento: " + str(aumento))
