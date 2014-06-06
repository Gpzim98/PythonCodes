def root13_dicionario(converter):
        retorno = ''
        alfabeto = {'a':'n', 'b':'o', 'c':'p','d':'q', 'e':'r', 'f':'s','g':'t','h':'u','i':'v','j':'w', 'k':'x','l':'y', 'm':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i', 'w':'j','x':'k','y':'l','z':'m'}
        for letra in converter:
            if letra in alfabeto or letra.lower() in alfabeto:
                if letra.islower():
                    retorno += alfabeto.get(letra)
                elif letra.isupper():
                    letra = letra.lower()
                    retorno += alfabeto.get(letra).capitalize()
            else:
                retorno += letra
        return retorno

def rot13_lista(converter):
    retorno=''
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for letra in converter:
        if letra in alfabeto or letra.lower() in alfabeto:
            j = alfabeto[(alfabeto.index(letra.lower()) + 13) % 26]
            if letra.islower():
                retorno += j
            else:
                retorno += j.upper()
        else:
            retorno += letra
    return retorno

def root13_string(s):
    lower_chars = ''.join(chr(c) for c in range (97,123)) #ASCII a-z
    upper_chars = ''.join(chr(c) for c in range (65,91)) #ASCII A-Z
    lower_encode = lower_chars[13:] + lower_chars[:13] #shift 13 bytes
    upper_encode = upper_chars[13:] + upper_chars[:13] #shift 13 bytes
    output = "" #outputstring
    for c in s:
        if c in lower_chars:
                output = output + lower_encode[lower_chars.find(c)]
        elif c in upper_chars:
            output = output + upper_encode[upper_chars.find(c)]
        else:
            output = output + c
    return output

def root13_com_2_listas(converter):
        converter = converter.lower()
        retorno=''
        alfabeto_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
        alfabeto_2 = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        for letra in converter:
            try:
                retorno += alfabeto_2[alfabeto_1.index(letra)]                
            except ValueError:
                try:
                    retorno += alfabeto_1[alfabeto_2.index(letra)]                
                except ValueError:
                    retorno += letra
        return retorno    