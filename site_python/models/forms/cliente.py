# coding: utf8
from web import form

ClientForm = form.Form(
    form.Textbox("Nome"),
    form.Textbox("Telefone",
                 form.notnull,
                 form.regexp('\d+', 'Digite um telefone'),
                 form.Validator('Seu telefone deve ter mais que 8 caracteres', lambda x: int(x) > 6)),
    form.Textarea('Digite um texto sobre voce'),
    form.Checkbox('Aceitos os termos de servico'),
    form.Dropdown('Sexo', ['Masculino', 'Feminino']))
