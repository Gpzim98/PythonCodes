 # -*- coding: utf8 -*-
__author__ = 'gpzim98'
import web
urls = (
    '/', 'hello', '/admin', 'admin'

)

app = web.application(urls, globals())
class hello:
    def GET(self):
        return 'Hello World'
    def POST(self):
        return 'Requisicao com post'

class admin:
    def GET(self):
        return """
               <!DOCTYPE html>
                    <html>
                        <body>

                            <div id="container" style="width:500px">

                                <div id="header" style="background-color:#FFA500;">
                                <h1 style="margin-bottom:0;">Main Title of Web Page</h1></div>

                                <div id="menu" style="background-color:#FFD700;height:200px;width:100px;float:left;">
                                <b>Menu</b><br>
                                HTML<br>
                                CSS<br>
                                JavaScript</div>

                                <div id="content" style="background-color:#EEEEEE;height:200px;width:400px;float:left;">
                                Content goes here</div>

                                <div id="footer" style="background-color:#FFA500;clear:both;text-align:center;">
                                Copyright © W3Schools.com</div>

                            </div>

                        </body>
                    </html>
               """
    def POST(self):
        return 'Admin'

application = app.wsgifunc()

#Verifica se o script esta executando diretamente ou se esta
#sendo importado dentro de outro modulo
#Evide de ao ser importado ja saia executando
if __name__ == "__main__":
    app.run()