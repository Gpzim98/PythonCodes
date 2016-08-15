class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x

'''
Por que o terceiro print imprimiu 323 ao inves de 311 ou 333?
Por que o Child1.x = 2 so mudou o valor de Chil1 e nao o valor de Child2?
Why last line of output is 3 2 3 rather than 3 2 1?

Por que em python os atributos das classes sao armezenados em dicionarios, se o python nao encontrar o
atributo na classe em questao (ou seja ainda nao esta definido) ele procura nas hierarquias acima (herancas)
ate encontar um valor assinalado
'''