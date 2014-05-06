# Calcula o quadrado dos
# numeros positivos em seq
seq = [ -1, 3, -5, 4, 8, 9 ]

# loop
res = []
for n in seq:
    if n > 0: res.append(n * n)
print res

# list comprehension
print [ x*x for x in seq if x > 0 ]
print [ x*x for x in seq ] # todos

# imprime ['nome: fulano', 'idade: 35']
d = { 'nome': 'fulano',
      'idade': '35' }
print [ "%s: %s" % (k,v) for \
            k,v in d.items() ]
