from bs4 import BeautifulSoup
import requests
import sys

url = 'http://www.youtube.com/results?search_query=%(q)s'


def buscar_links(url):
    lista = []
    i = 0
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    for a in soup.findAll('a', href=True):
        link = a['href']
        i += 1
        lista.append(link)
        links = str(link).strip('[]').replace("u", "").replace("'", "")
        print str(i) + ") " + str(links)
    print "\n>> Total = %d \n" % i
    sys.exit()

for arg in sys.argv:
    if arg == "-l":
        url = raw_input('>> Busca')
        buscar_links(url)
