"""
Este programa muestra diferentes operaciones con tuplas en Python:

1. Crear una nueva tupla a partir de la concatenación de dos tuplas.
2. Convertir una lista en tupla usando la función tuple().
3. Obtener una subtupla mediante slicing.
4. Desempaquetar los elementos de una tupla en variables.
5. Recorrer una tupla con un bucle for.
6. Convertir una tupla en lista usando la función list().

Finalmente, se imprimen los resultados de cada operación.
"""

# Crea una tupla a partir de la concatenacion de dos tuplas
numeros = (1, 2, 3) + (4, 5 , 6)
print(numeros)

# Crea una tupla a partir de una lista
punto = tuple([1, 2])
print(punto)

# Crea una tupla con los dos primeros elementos de otra tupla
menosNumeros = numeros[:2]
print(menosNumeros)

# Crea tres variables a partir de una tupla
primero, segundo, *resto = numeros
print(primero, segundo, resto)

# Itera sobre una tupla
for i in numeros:
    print(i)

# Crea una lista a partir de una tupla
numerosList = list(numeros)
print(numerosList)

