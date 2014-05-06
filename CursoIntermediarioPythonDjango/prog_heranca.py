class ClassePai1(object):
    def metodo(self, param):
        print "Classe pai 1:", param

class ClassePai2(object):
    def metodo(self, param):
        print "Classe pai 2:", param

class ClasseFilha(ClassePai1, ClassePai2):
    def metodo(self, param):
        super(ClasseFilha, self).metodo(param)
        print "Classe filha:", param

filha = ClasseFilha()
filha.metodo("mensagem")
