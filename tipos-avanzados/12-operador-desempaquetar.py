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
# Se puede combinar con elementos adicionales
nuevoPunto = {**punto1, "hola": "mundo", **punto2}
print(nuevoPunto)
