mascotas = [
    'gatito',
    'perro',
    'pez',
    'gato',
    'pez',
    'conejo'
]
mascotas.insert(1, "Melvin")
mascotas.append("conejita")

mascotas.remove("pez")
mascotas.pop(1)
del mascotas[0]
mascotas.clear()
print(mascotas)