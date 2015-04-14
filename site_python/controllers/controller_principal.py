from models.forms.cliente import ClientForm
import web


class Home(object):

    def __init__(self):
        self.templates = web.template.render('templates/')

    def GET(self):
        i = web.input(name="Gregory")

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

    def GET(self):
        return self.templates.admin.index(name='Gregory')

    def POST(self):
        return 'Admin'
