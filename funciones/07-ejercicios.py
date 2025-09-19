"""
Función para comprobar si un texto es un palíndromo
(un texto que se lee igual de izquierda a derecha que de derecha a izquierda).

- es_palindromo(texto):
    1. Recorre el texto original y crea 'texto_sin_espacios' sin espacios,
       convirtiendo cada carácter a minúscula.
    2. Genera 'texto_reversa' invirtiendo el orden de 'texto_sin_espacios'.
    3. Devuelve True si ambos textos coinciden (es palíndromo) o False en caso contrario.

- Ejemplos de uso:
    - "Abba"  → True
    - "Reconocer" → True
    - "Amo la paloma" → True
    - "Hola mundo" → False
"""

# Definimos una funcion que nos dice si un texto es palindromo (que se lee igual al derecho que al reves)
def es_palindromo(texto):
    texto_sin_espacios = "" # Variable que almacenara el texto sin espacios
    for i in texto:
        if i == " ": continue
        else:
            texto_sin_espacios += i.lower() # Agregamos el caracter iterado, en minuscula con la funcion lower()
    texto_reversa = "" # Variable que almacenara el texto_sin_espacios en reversa
    for i in texto_sin_espacios[::-1]:
        texto_reversa += i
    return texto_sin_espacios == texto_reversa # Retorna un booleando comprobando si es True o False que el texto_sin_espacios sea igual a texto_reversa y sea palindromo


# Imprimimos varios textos para comprobar si son palindromos gracias a la funcion que definimos
print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola mundo", es_palindromo("Hola mundo"))

