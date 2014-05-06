def potencia(x, y=2):
    return x ** y

def sem_return():
    pass

descricao = {
    'txt': "Arquivo texto",
    'html': "Arquivo HTML" }

mime_type = {
    'txt': "text/plain",
    'html': "text/html" }

def arquivo(extensao):
    return descricao[extensao], mime_type[extensao]

print potencia(5) # 25
print sem_return() # None
print arquivo('txt') # ('Arquivo texto', 'text/plain')
