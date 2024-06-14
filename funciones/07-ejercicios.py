def es_palindromo(texto):
    texto_sin_espacios = ""
    for i in texto:
        if i == " ": continue
        else:
            texto_sin_espacios += i.lower()
    texto_reversa = ""
    for i in texto_sin_espacios[::-1]:
        texto_reversa += i
    return texto_sin_espacios == texto_reversa
            
    
    
print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola mundo", es_palindromo("Hola mundo"))