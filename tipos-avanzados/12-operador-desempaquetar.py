"""
Este programa muestra cómo utilizar los operadores de desempaquetado * y ** en Python:

1. El operador * desempaqueta listas o tuplas:
   - Permite imprimir o combinar elementos de forma individual.
   - Se puede usar junto con otros valores para crear nuevas listas o tuplas.

2. El operador ** desempaqueta diccionarios:
   - Combina varios diccionarios en uno solo.
   - Si hay claves repetidas, se conserva el valor del último diccionario desempaquetado.
   - También puede combinarse con claves adicionales personalizadas.

Finalmente, se imprimen los resultados de las combinaciones.
"""

# * sirve para desempaquetar una lista o tupla, es decir, para obtener los elementos de una lista o tupla de forma individual.
lista = [1, 2, 3, 4, 5]
print(*lista)

# Se puede usar para combinar listas o tuplas
# Se puede combinar con elementos adicionales
lista2 = [5, 6]

combinada = [*lista, "hola", *lista2, "mundo"]
print(combinada)


# ** sirve para desempaquetar diccionarios, desempaqueta de derecha a izquierda por eso toma primero el valor de "y" del punto2.
# Si se repiten las claves, se toma el valor del último diccionario.
punto1 = {"x": 19, "y": 20}
punto2 = {"y": 15}
print({**punto1, **punto2})

# Se puede combinar con elementos adicionales
nuevoPunto = {**punto1, "hola": "mundo", **punto2}
print(nuevoPunto)

