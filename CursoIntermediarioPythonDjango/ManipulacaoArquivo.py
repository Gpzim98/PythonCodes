end = raw_input("Informe o caminho do arquivo: ")

#import pdb
#pdb.set_trace()
f = file(end)

#Seta ponteiro de leitura no inicio do arquivo
f.seek(0)

for linha in f:
	print linha.strip()

print '---LENDO O ARQUIVO TODO DE UMA VEZ---'
f.seek(0)
pegandoTodasAsLinhas = f.readlines()
print pegandoTodasAsLinhas


print '---LENDO O ARQUIVO BIT A BIT---'
f.seek(0)
for letras in f.read(3):
	print letras
f.close()


print '---ESCRITA---'
f = open(end,"a")
f.write(raw_input("Digite algo para ser escrito no arquivo"))
f.close()

f = open(end,"r")
linhaToda = f.readlines()
print linhaToda



