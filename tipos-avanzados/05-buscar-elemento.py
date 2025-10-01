"""
Ejemplo de métodos de listas en Python:

- Se define una lista 'mascotas' con 6 elementos.
- count(x): devuelve cuántas veces aparece 'x' en la lista.
- index(x): devuelve el índice de la primera aparición de 'x'.
    • Si el elemento no existe, lanza un error.
    • Por eso se usa 'if "pez" in mascotas:' antes de llamar a index().
"""

# Declaramos una lista con 6 elementos
mascotas = ['perro', 'pez', 'gato', 'loro', 'pez', 'conejo']

# count nos permite contar cuantas veces se repite un elemento en la lista
print(mascotas.count('pez'))

# index nos permite buscar un elemento en la lista pero solo nos devuelve el primer indice donde se encuentra
if "pez" in mascotas:
    print(mascotas.index("pez"))

