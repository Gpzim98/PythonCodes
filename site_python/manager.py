 # -*- coding: utf8 -*-
__author__ = 'gpzim98'

import web

from controllers.controller_principal import Home, Admin, OutraPagina

urls = (
    '/', 'Home',
    '/admin/(.*)', 'Admin',
    '/teste/', 'OutraPagina'
)

app = web.application(urls, globals())

application = app.wsgifunc()

#Verifica se o script esta executando diretamente ou se esta
#sendo importado dentro de outro modulo
#Evide de ao ser importado ja saia executando
if __name__ == "__main__":
    app.run()
