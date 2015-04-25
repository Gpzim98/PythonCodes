from bs4 import BeautifulSoup
import requests

url = 'http://www.youtube.com/results?search_query=%(q)s'

busca = {
    'q': raw_input('>> Buscar: '),
}

r = requests.get(url % busca)
soup = BeautifulSoup(r.text)

titulo = [title.text for title in soup.findAll('h3')]

for t in titulo:
    print(t)
