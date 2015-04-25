# coding: utf8
from bs4 import BeautifulSoup
import requests
import codecs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from time import gmtime, strftime


def send_email(assunto, mensagem):
    me = "contato@gregorypacheco.com.br"
    you = 'contato@gregorypacheco.com.br, gpzim98@gregorypacheco.com.br'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = assunto
    msg['From'] = me
    msg['To'] = you

    text = assunto
    html = mensagem

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    s = smtplib.SMTP('gregorypacheco.com.br', port=25)
    s.sendmail(me, you, msg.as_string())
    s.quit()

vagas = 96

def crow(vagas):
    fichier = codecs.open('saida_classificados.txt', "w", encoding="utf-8")
    #fichierTemp = codecs.open("tempASCII", "w", encoding="ascii", errors="ignore")

    url = 'http://jornaloportunidades.com/montesclaros/classificados/102/empregos_oferta/'

    r = requests.get(url)

    soup = BeautifulSoup(r.text)
    #titulo = [title.text for title in soup.find_all(attrs={"class": "anuncios "})]
    num_vagas = soup.find("strong")
    fichier.write(u'Número de vagas atual: ' + num_vagas.text + '\n')

    fichier.write(u'Últimas 3 vagas')

    for t in soup.find_all(attrs={"class": "anuncios "}, limit=3):
        fichier.write(t.text)

    fichier.write('\n')
    fichier.close()

    if vagas > 96:
        send_email(u'Nova vaga de emprego', url)
        return vagas + 1

    time.sleep(10)

while True:
    log = codecs.open('log_classificados.log', "w", encoding="utf-8")
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())
    log.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    log.close()
    vagas = crow(vagas)
