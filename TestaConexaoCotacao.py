#coding:utf-8
import urllib
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime as date


STR_VERIFY = '<schema targetNamespace="http://bean.model.com.br" xmlns="http://www.w3.org/2001/XMLSchema0">'


def send_email(assunto, mensagem):
        me = "gpzim98@gmail.com"
        you = "gregory@atsinformatica.com.br"

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

        s = smtplib.SMTP('smtp.atsinformatica.com.br')
        s.sendmail(me, you, msg.as_string())
        s.quit()


def grava_log(mensagem):
        arq = open('log_verificacao_web_cotacao.txt', 'a')
        arq.write(mensagem + '\n')
        arq.close()

i = 0
cont = 0
mensagem = ''
tmp_now = ''
while True:
        tmp_now = date.today().strftime("%d de %B de %G - %H:%M:%S")
        a = urllib.urlopen(
                'http://cotacao.atscelular.com.br:32100/WebServiceCotacaoPreco/wsdl/MetodoWebService.wsdl')
        os.system('clear')
        if STR_VERIFY in a.read():
                mensagem = u'Connected - ' + tmp_now
                print mensagem
                grava_log(mensagem)
                if i == 240:
                        i = 0
                        send_email(u'Sitema de cotacao - OK - Linode','Servidor Ok - '+ tmp_now)
        else:
                send_email(u"Sistema de cotacao - FALHA - Linode", 'Server is broken down - ' + tmp_now)
                mensagem = u'FAILED TO CONNECT - ' + tmp_now
                print mensagem
                grava_log(mensagem)
        a.close()
        i += 1
        time.sleep(180)
