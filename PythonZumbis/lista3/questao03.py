a = 80000
b = 200000
anos = 0
while a < b:
    a *= 0.03 * a
    b *= (0.015*b)
    anos += 1

print "Anos necessarios: ", anos
