# Declaramos una lista con 6 elementos
mascotas = ['perro', 'pez', 'gato', 'loro', 'pez', 'conejo']

# count nos permite contar cuantas veces se repite un elemento en la lista
print(mascotas.count('pez'))

# index nos permite buscar un elemento en la lista pero solo nos devuelve el primer indice donde se encuentra
if "pez" in mascotas:
    print(mascotas.index("pez"))
