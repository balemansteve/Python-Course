"""
Este programa muestra cómo recorrer, transformar y filtrar listas en Python usando bucles, comprensión de listas,
y funciones lambda con map() y filter().

1. Se crea una lista de usuarios con su nombre y calificación.
2. Se extraen los nombres usando un bucle for y el método append().
3. Se realiza la misma extracción mediante comprensión de listas.
4. Se aplican ejemplos de filtrado y transformación:
   - Filtrar usuarios con calificación mayor a 2.
   - Usar funciones lambda junto con map() y filter().

Finalmente, se imprimen los resultados para observar los cambios en las listas.
"""

# Declaramos una lista de usuarios
usuarios = [
    ["Bryan", 4], 
    ["Juan", 2], 
    ["Ana", 3], 
    ["Carlos", 1]
]

# Declaramos una lista nombres[], con el metodo append() le vamos agregando el primer elemento de cada sublista de la lista usuarios[]
nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)

# nombres = [expresion for i in items]
# Transformacion - map

# Declaramos una lista, para cada sublista de la lista usuarios[] vamos guardando el segundo elemento de cada sublista en la lista creada
nombres = [usuario[1] for usuario in usuarios]
print(nombres)

# Filtramos - filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# Filtrar y transformar
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# Filtrar y transformar - con lambda usando la funcion map y filter
# nombres = list(map(lambda usuario: usuario[0], usuarios))

menosUsuario = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuario)

# print(nombres)

