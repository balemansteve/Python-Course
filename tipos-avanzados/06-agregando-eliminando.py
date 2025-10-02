"""
Ejemplo de operaciones comunes sobre listas en Python:

- insert(i, x): inserta 'x' en la posición 'i'.
- append(x): agrega 'x' al final de la lista.
- remove(x): elimina la primera aparición de 'x'.
- pop(i): elimina el elemento en el índice 'i' y lo devuelve.
- del lista[i]: elimina el elemento en el índice 'i'.
- clear(): elimina todos los elementos de la lista.
"""

# Declara una lista de 6 elementos
mascotas = [
    'gatito',
    'perro',
    'pez',
    'gato',
    'pez',
    'conejo'
]

# Agrega un elemento en el indice 1 de la lista
mascotas.insert(1, "Melvin")
print(mascotas)

# Agrega un elemento al final de la lista
mascotas.append("conejita")
print(mascotas)

# Elimina el primer elemento que coincida con el valor dado
mascotas.remove("pez")
print(mascotas)

# Elimina el elemento en el indice dado
mascotas.pop(1)
print(mascotas)

# Elimina el elemento en el indice dado
del mascotas[1]
print(mascotas)

# Elimina todos los elementos de la lista
mascotas.clear()
print(mascotas)

