from modeller import *
 
env = environ()
aln = alignment(env)
mdl = model(env, file='1R26', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1r26_A', atom_files='1R26.pdb')
arquivo = raw_input("Informe o caminho+nome do arquivo")
aln.append(file=arquivo, alignment_format='FASTA', align_codes='LbrM.01.0300')
aln.align2d()
aln.write(file='LbrM.01.0300-1r26_A.ali', alignment_format='PIR')
aln.write(file='LbrM.01.0300-1r26_A.pap', alignment_format='PAP')
aln.write(file='LbrM.01.0300-1r26_A.fasta', alignment_format='FASTA')