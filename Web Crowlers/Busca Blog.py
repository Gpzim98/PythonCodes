# coding: utf8
from bs4 import BeautifulSoup
import requests
import codecs

fichier = codecs.open('saida_blog.txt', "w", encoding="utf-8")
#fichierTemp = codecs.open("tempASCII", "w", encoding="ascii", errors="ignore")


url = 'http://blog.gregorypacheco.com.br/?page=%d'

page_number = 1

r = requests.get(url % page_number)

#arquivo = open('', 'w')

while r.ok:
    soup = BeautifulSoup(r.text)
    titulo = [title.text for title in soup.findAll('h2')]

    for t in titulo:
        fichier.write(str(page_number) + ' - ' + t + '\n')

    page_number = page_number + 1
    r = requests.get(url % page_number)

fichier.close()
