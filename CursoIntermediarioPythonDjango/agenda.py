#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from Dialog import Dialog
import shelve


class MainFrame(Frame):

    def __init__(self, parent=None):
        super(MainFrame, self).__init__(parent)
        self.grid()
        self.createWidgets()
        self.master.title("Cadastro de amigos")

    def createWidgets(self):
        self.makeScreen()
        self.makeToolBar()

    def makeScreen(self):
        self.nome = StringVar()
        self.endereco = StringVar()
        self.telefone = StringVar()

        Label(self, text="Nome:").grid(row=1, sticky=W)
        Label(self, text="Endereço:").grid(row=2, sticky=W)
        Label(self, text="Telefone:").grid(row=3, sticky=W)

        Entry(self, textvariable=self.nome).grid(
            row=1, column=1, sticky=W + E)
        Entry(self, textvariable=self.endereco).grid(
            row=2, column=1, sticky=W + E)
        Entry(self, textvariable=self.telefone).grid(
            row=3, column=1, sticky=W + E)

    def makeToolBar(self):
        toolbar = Frame(self)
        toolbar.grid(row=4, columnspan=2)

        Button(toolbar, text="Adicionar",
               command=self.adicionar).grid(row=0, column=0)
        Button(toolbar, text="Gravar",
               command=self.gravar).grid(row=0, column=1)
        Button(toolbar, text="Remover",
               command=self.remover).grid(row=0, column=2)
        Button(toolbar, text="Procurar",
               command=self.procurar).grid(row=0, column=3)
        Button(toolbar, text="Listar",
               command=self.listar).grid(row=0, column=4)
        Button(toolbar, text="Sair",
               command=self.sair).grid(row=0, column=5)

    def adicionar(self):
        nome = self.nome.get()
        if not nome:
            Dialog(self, title="Erro!", text="Nome inválido",
                   bitmap='error', default=0, strings=('OK',))
            return

        if nome in self.db:
            Dialog(self, title="Erro!", text="Nome já cadastrado",
                   bitmap='error', default=0, strings=('OK',))
            return

        self.db[nome] = (self.endereco.get(), self.telefone.get())
        self.limpaCampos()

    def gravar(self):
        nome = self.nome.get()
        if not nome:
            Dialog(self, title="Erro!", text="Nome inválido",
                   bitmap='error', default=0, strings=('OK',))
            return

        if nome not in self.db:
            Dialog(self, title="Erro!",
                   text="Nome inexistente, use o botão adicionar",
                   bitmap='error', default=0, strings=('OK',))
            return

        self.db[nome] = (self.endereco.get(), self.telefone.get())
        self.limpaCampos()

    def limpaCampos(self):
        self.nome.set("")
        self.telefone.set("")
        self.endereco.set("")

    def procurar(self):
        nome = self.nome.get()
        if not nome:
            Dialog(self, title="Erro!", text="Nome inválido",
                   bitmap='error', default=0, strings=('OK',))
            return

        if nome not in self.db:
            Dialog(self, title="Erro!", text="Nome não encontrado",
                   bitmap='error', default=0, strings=('OK',))
            return

        self.endereco.set(self.db.get(nome, "")[0])
        self.telefone.set(self.db.get(nome, "")[1])

    def remover(self):
        nome = self.nome.get()
        if not len(nome):
            Dialog(self, title="Erro!", text="Nome inválido",
                   bitmap='error', default=0, strings=('OK',))
            return

        if not self.db.has_key(nome):
            Dialog(self, title="Erro!", text="Nome não encontrado",
                   bitmap='error', default=0, strings=('OK',))
            return

        self.endereco.set(self.db.get(nome, "")[0])
        self.telefone.set(self.db.get(nome, "")[1])

        resposta = Dialog(self, title="Confirmação",
                          text="Deseja remover?",
                          bitmap='question', default=1, strings=('Sim', 'Não'))
        if resposta.num == 0:
            del self.db[nome]
            self.limpaCampos()

    def listar(self):
        print "%-30s | %-20s | %-10s" % ("Nome", u"Endereço", "Telefone")
        print "%-30s-+-%-20s-+-%-10s" % ("-" * 30, "-" * 20, "-" * 10)
        for k in self.db:
            print "%-30s | %-20s | %-10s" % (k, self.db[k][0],
                                             self.db[k][1])
        print

    def sair(self):
        resposta = Dialog(self, title="Confirmação",
                          text="Tem certeza que deseja sair?",
                          bitmap='question', default=1,
                          strings=('Sim', 'Não'))
        if resposta.num == 0:
            self.quit()

    def setDB(self, db):
        self.db = db


def main():
    db = shelve.open("teste.db")
    frm = MainFrame()
    frm.setDB(db)
    frm.mainloop()
    db.close()

if __name__ == '__main__':
    main()
