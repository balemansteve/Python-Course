"""
Este programa muestra diferentes formas de ordenar listas en Python:

1. Se ordena una lista de números utilizando:
   - sort(): ordena la lista directamente (in place).
   - sorted(): crea una nueva lista ordenada.

2. Se trabaja con una lista de usuarios con calificaciones y se ordena:
   - Mediante una función que devuelve el segundo elemento de cada sublista.
   - Con una función lambda para simplificar el código.

Finalmente, se imprimen los resultados ordenados en pantalla.
"""

# Declaramos una lista de numeros
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Dos formas de ordenar una lista:

# Sort ordena la lista de menor a mayor, el parametro reverse=True la ordena de mayor a menor
numeros.sort(reverse=True)
print(numeros)

# Sorted crea una nueva lista ordenada de menor a mayor, el parametro reverse=True la ordena de mayor a menor
numeros2 = sorted(numeros, reverse=True)
print(numeros2)

# Declarar una lista de usuarios con su calificacion
usuarios = [["Bryan", 4], ["Juan", 2], ["Ana", 3], ["Carlos", 1]]

# Definir una funcion que regrese el segundo elemento de la sublista
def ordena(elemento):
    return elemento[1]

# Este algoritmo obtiene la calificacion del primer usuario mediante la funcion ordena
# primer_usuario = usuarios[0]
# calificacion = ordena(primer_usuario)
# print(calificacion)

# Ordenar la lista de usuarios de mayor a menor calificacion con la funcion ordena
# usuarios.sort(key=ordena, reverse=True)

# Ordenar la lista de usuarios de mayor a menor calificacion con una funcion lambda
usuarios.sort(key=lambda elemento: elemento[1], reverse=True)
print(usuarios)

