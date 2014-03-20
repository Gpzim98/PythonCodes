# encoding: utf-8
__author__ = 'gpzim98'
from abc import ABCMeta, abstractmethod
class ClasseAbstrata(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def meu_metodo_abstrato(self):
        print 'My abstract method'

#As duas linhas abaixo irão gerar o erro de instância de classe abstrata
a = ClasseAbstrata()
a.meu_metodo_abstrat()
