class Abstrata:
    def metodo_abstrato(self):
        pass

try:
    print 1 / 0
except ZeroDivisionError:
    pass # ignora
