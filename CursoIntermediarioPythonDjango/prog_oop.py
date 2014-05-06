class Pessoa(object):
  def __init__(self, nome):
    self.nome = nome

  def valida(self):
    raise NotImplementedError("Abstrata")

class PessoaFisica(Pessoa):
  tabela_db = "pessoa_fisica"
  def __init__(self, nome, cpf):
    super(PessoaFisica, self).__init__(nome)
    self.cpf = ''.join(\
            d for d in cpf if d.isdigit()
        )

  def valida(self):
    return len(self.cpf) == 11

class PessoaJuridica(Pessoa):
  tabela_db = "pessoa_juridica"
  def __init__(self, nome, cnpj):
    super(PessoaJuridica, self).__init__(nome)
    self.cnpj = ''.join(\
            d for d in cnpj if d.isdigit()
        )

  def valida(self):
    return len(self.cnpj) == 14

fulano = PessoaFisica("Fulano", "123.456.789-01")
acme = PessoaJuridica("ACME", "12.345.678/0001-90")

print fulano.nome, fulano.cpf, fulano.valida()
print acme.nome, acme.cnpj, acme.valida()

