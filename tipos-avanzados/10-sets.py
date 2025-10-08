"""
Este programa demuestra el uso de conjuntos (set) en Python:

1. Crea un conjunto, mostrando que los elementos duplicados se eliminan automáticamente.
2. Convierte una lista en conjunto utilizando la función set().
3. Realiza operaciones entre conjuntos:
   - Unión (|): combina los elementos de ambos conjuntos.
   - Intersección (&): obtiene los elementos comunes.
   - Diferencia (-): muestra los elementos del primer conjunto que no están en el segundo.
   - Diferencia simétrica (^): muestra los elementos que no se repiten en ambos conjuntos.

Finalmente, se imprimen los resultados de cada operación.
"""

# set significa grupo o conjunto
# solo hay una instancia de cada elemento
primer = {1, 1, 2, 3, 4}
# primer.add(5)
# # primer.remove(1)
print(primer)

# Crea un set a partir de una lista
segundo = [3, 4, 5]
segundo = set(segundo)
print(segundo)

# Imprime la union de los dos sets (operador union '|')
print(primer | segundo)

# imprime la interseccion de los dos sets (operador interseccion '&')
# son los elementos que estan en ambos sets
print(primer & segundo)

# imprime la diferencia de los dos sets (operador diferencia '-')
# son los elementos que estan en el primer set pero no en el segundo, es decir que quita del primer set los elementos que esten en el segundo
print(primer - segundo)

# imprime la diferencia simetrica de los dos sets (operador diferencia simetrica '^')
# son los elementos que no se repiten en ambos sets
print (primer ^ segundo)

