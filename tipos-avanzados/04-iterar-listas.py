# Declaramos una lista con 5 elementos
mascotas = ['perro', 'gato', 'loro', 'pez', 'conejo']

# Iteramos la lista de mascotas
# Enumerate nos devuelve el indice y el valor de la lista
for indice, mascota in enumerate(mascotas):
    # Imprimimos el indice y el valor de la lista
    print(indice, mascota)