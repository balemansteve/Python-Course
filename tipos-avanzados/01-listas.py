"""
Demostración de creación y manipulación de listas en Python:

- Se definen listas con distintos tipos de datos:
    numeros, letras, palabras, booleans y matriz (listas anidadas).
- Creación de listas repetidas:
    ceros = [0] * 10         → lista con diez ceros
    cero_y_uno = [0, 1] * 10 → repite la secuencia 0,1 diez veces.
- Concatenación de listas con el operador +:
    alfanumerico = numeros + letras
- Uso de la función list():
    • list(range(1, 11)) convierte un rango en una lista de 1 a 10.
    • list("hola mundo") convierte cada carácter de la cadena en un elemento de lista.
"""

# Declaramos varias listas con diferentes tipos de datos
numeros = [1, 2, 3]
letras = ["a", "b", "c"]
palabras = ["Hola", "Mundo", "Python"]
booleans = [True, False, True]
matriz = [[0, 1], [2, 3], [4, 5]]
ceros = [0] * 10
cero_y_uno = [0, 1] * 10

# Concatenamos listas
alfanumerico = numeros + letras

# funcion list() retorna una lista de un iterable

# funcion list() que toma el retorno de la funcion range() y lo convierte en una lista
rango = list(range(1, 11))
print(rango)

# funcion list() para convertir un string en una lista 
chars = list("hola mundo")
print(chars)

