ano = input("Ano: ")

if (int(ano) % 4) != 0:
    print "Nao e bissexto"
else:
    if str(ano)[2:4] != "00":
        print "Bissexto"
    else:
        if (int(ano) % 400) == 0:
            print "Bissexto"
        else:
            print "Nao e bissexto"
