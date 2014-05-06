import sys

for linha in sys.stdin:
    if not linha.strip():
        continue
    if "FIM" in linha:
        break
    print "#", linha.rstrip()
else:
    print "# FIM DO ARQUIVO"
