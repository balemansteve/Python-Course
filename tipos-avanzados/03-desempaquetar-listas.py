"""
Ejemplo de desempaquetado de listas:

- Se define una lista con 5 números.
- El desempaquetado asigna elementos de la lista a variables:
    primero, *otros, penultimo, ultimo = numeros
    • 'primero' toma el primer elemento.
    • 'ultimo' toma el último elemento.
    • 'penultimo' toma el penúltimo elemento.
    • '*otros' recibe en una lista todos los elementos restantes del medio.
- Se imprimen las variables para mostrar el resultado del desempaquetado.
"""

# Declaramos una lista con 5 números
numeros = [1, 2, 3, 4, 5]

# Asi no, aqui lo que ocurre es que se crea una lista para cada variable.
# primero = [0]
# segundo = [1]
# tercero = [2]

# Desempaquetamos la lista en tres variables pero da error si no hay la misma cantidad de variables que de elementos en la lista
# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

# Desempaquetamos la lista en tres variables y el resto de los elementos en una lista llamada otros
primero, *otros, penultimo, ultimo = numeros
# Improprime los valores de las variables
print(primero, penultimo, ultimo)
print(otros)

