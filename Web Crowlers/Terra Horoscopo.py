from bs4 import BeautifulSoup
import requests
import urllib2
import re

site = 'http://vidaeestilo.terra.com.br/esoterico/interna/0,,OI4065934-EI14316,00-Capa+horoscopo.html'
r = requests.get(site)
soup = BeautifulSoup(r.text)

print '\nDigite o seu signo com a primeira letra em maiusculo.'
signo = raw_input('>> ')

for a in soup.findAll('a', {'title': signo}):
    link = a['href']
    print link
    html = urllib2.urlopen(link).read()
    soup = BeautifulSoup(html)
    for p in soup.findAll('p'):
        regex = re.compile(r'<[^<]*?>')
        descricao = regex.sub('', str(p))
        print '============================'
        print '\n' + descricao
