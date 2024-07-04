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