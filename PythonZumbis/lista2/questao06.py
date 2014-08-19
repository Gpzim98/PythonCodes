ganho_hora = input("Ganho por hora: ")
horas_mes = input("Horas trabalhadas por mes: ")

salario = ganho_hora * horas_mes
inss = salario * 0.08
ir = salario * 0.11
sindicato = salario * 0.05

print "Salario bruto: ", salario
print "Valor do IR: ", ir
print "Valor do INSS: ", inss
print "Valor do Sindicado: ", sindicato
print "Salario liquido do mes: ", salario - inss - ir - sindicato
