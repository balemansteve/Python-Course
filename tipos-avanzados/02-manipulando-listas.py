"""
Ejemplo de operaciones con listas:

- Se crea una lista 'mascotas' con 4 elementos.
- Se accede a un elemento por índice:
    mascotas[0] → primer elemento.
- Se modifica un elemento:
    mascotas[0] = "Bicho".
- Se usan rebanadas (slicing):
    mascotas[::2] → imprime cada 2 elementos (índices 0 y 2).
    mascotas[-1]  → último elemento.
- Se crea una lista de números del 0 al 20 con range() y list().
- Se imprimen solo los números pares:
    numeros[2::2] → comienza en índice 2 y avanza de 2 en 2.
"""

# Declara una lista con 4 elementos
mascotas = ['perro', 'gato', 'pez', 'tortuga']

# Imprime el primer elemento de la lista
print(mascotas[0])

# Cambia el primer elemento de la lista
mascotas[0] = "Bicho"
print(mascotas)

# Imprime los ultimos dos elementos de la lista
print(mascotas[::2])

# Imprime el ultimo elemento de la lista
print(mascotas[-1])

# Declara una lista con los numeros del 0 al 20
numeros = list(range(21))
# Imprime los numeros pares de la lista
print(numeros[2::2])

