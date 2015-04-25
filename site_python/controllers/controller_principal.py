from models.forms.cliente import ClientForm
import web


class Home(object):

    def __init__(self):
        self.templates = web.template.render('templates/')

    def GET(self):

        form = ClientForm()

        return self.templates.index(form)

    def POST(self):
        form = ClientForm()
        if not form.validates():
            return self.templates.index(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            return "Great! boe: %s, bax: %s" % (form.d.Nome, form['Telefone'].value)


class Admin(object):

    def __init__(self):
        self.templates = web.template.render('templates/')

    def GET(self, name):
        i = web.input(name=None)
        return self.templates.admin.index(i.name)

    def POST(self):
        return 'Admin'


class OutraPagina(object):

    def __init__(self):
        self.templates = web.template.render('templates/')

    def GET(self):
        name = 'Greg'
        return self.templates.teste(name)

    def POST(self):
        i = web.input()
        firstname = i['firstname']
        lastname = i['lastname']
        frase = 'Seja bem vindo %s %s' % (firstname, lastname)
        return self.templates.teste(frase)
