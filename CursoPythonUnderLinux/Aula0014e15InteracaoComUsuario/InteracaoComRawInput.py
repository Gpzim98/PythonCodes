print type(10)

s1 = raw_input("Digite o primeiro numero: ")
s2 = raw_input("Digite o segundo numero: ")
soma = int(s1) + int(s2)
print 'Resultado: %(s1)s + %(s2)s = %(soma)d'%locals()

s1 = raw_input("Digite o primeiro numero: ")
s2 = raw_input("Digite o segundo numero: ")
soma = float(s1) + float(s2)
print 'Resultado: %(s1)s + %(s2)s = %(soma)f'%locals()
