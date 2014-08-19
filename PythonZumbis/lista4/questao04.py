lista = """
    The Python Software Foundation and the global Python
    community welcome and encourage participation by everyone
    Our community is based on mutual respect tolerance and encouragement
    and we are working to help each other live up to these principles
    We want our community to be more diverse whoever you are and whatever your
    background we welcome you
""".lower().split()

i = 0
lista2 = []

while i < len(lista):
    if lista[i][0] in "Python" or lista[i][-1] in "Python":
        lista2.append(lista[i])
    i += 1

print lista2
