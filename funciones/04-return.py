"""
Ejemplo de función que devuelve un valor:

- Se define la función suma(a, b) que recibe dos argumentos y retorna su suma.
- Se puede guardar el resultado de la función en una variable para usarlo
  en cálculos posteriores.
- En este ejemplo:
    1. c = suma(1, 2) guarda 3
    2. d = suma(c, 2) guarda 5
- Finalmente se imprime el resultado final (5).
"""

# Definimos una funcion que recibe dos argumentos y devuelve la suma de ambos
def suma(a, b):
    resultado = a + b
    return resultado

# Llamamos a la función que definimos anteriormente para sumar dos números y guardamos el resultado en una variable
c = suma(1, 2)
d = suma(c, 2)

print(d)

