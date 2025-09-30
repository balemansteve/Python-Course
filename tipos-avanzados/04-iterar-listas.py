"""
Ejemplo de iteración de una lista con enumerate:

- Se define una lista 'mascotas' con 5 elementos.
- El bucle for usa enumerate(mascotas) para recorrer la lista.
    • enumerate() devuelve tuplas (índice, valor) en cada iteración.
- Se imprimen el índice y el nombre de cada mascota.
"""

# Declaramos una lista con 5 elementos
mascotas = ['perro', 'gato', 'loro', 'pez', 'conejo']

# Iteramos la lista de mascotas
# Enumerate nos devuelve el indice y el valor de la lista
for indice, mascota in enumerate(mascotas):
    # Imprimimos el indice y el valor de la lista
    print(indice, mascota)

