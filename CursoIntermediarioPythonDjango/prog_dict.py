notas_alunos = {
   "Graham Chapman": 5.5,
   "John Cleese": 7.0,
   "Terry Gilliam": 4.5,
   "Terry Jones": 4.5,
   "Eric Idle": 10,
   "Michael Palin": 3.5,
}

print "Conteudo do dicionario:", notas_alunos
print "Chaves do dicionario:", notas_alunos.keys()
print "Valores do dicionario:", notas_alunos.values()
print "Items do dicionario:", notas_alunos.items()
print "-" * 20

for aluno in notas_alunos:
   print aluno

for nota in notas_alunos.values():
   print nota
for aluno, nota in notas_alunos.items():
   print "Aluno: %-20s  Nota: %4.1f" % (aluno, nota)
