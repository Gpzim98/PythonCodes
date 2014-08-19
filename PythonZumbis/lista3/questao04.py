tam_seq = input("Informe o tamanho da sequencia: ")
for x in range(tam_seq):
    a, b = 0, 1
    for i in range(x):
        a, b = b, a+b
    print a
