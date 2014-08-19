lista = """
    The Python Software Foundation and the global Python
    community welcome and encourage participation by everyone
    Our community is based on mutual respect tolerance and encouragement
    and we are working to help each other live up to these principles
    We want our community to be more diverse whoever you are and whatever your
    background we welcome you
""".lower().split()

i = 0
conta_palavras = 0

while i < len(lista):
    if "p" in lista[i] or "y" in lista[i]  or "t" in lista[i] or "h" in lista[i] or "o" in lista[i] or "n" in lista[i]:
        if len(lista[i]) > 4:
            conta_palavras += 1
    i += 1

print conta_palavras
