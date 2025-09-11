"""
Ejemplo de función con número variable de argumentos (*args):

- Se define la función suma(*numeros), donde *numeros permite recibir
  cualquier cantidad de argumentos como una tupla.
- Dentro de la función, se recorren los valores y se van sumando en 'resultado'.
- Finalmente, se imprime la suma total.

- Se llama a la función con diferentes cantidades de argumentos, 
  mostrando que *args se adapta a cada caso.
"""

# Definimos una función que recibe un número variable de argumentos, suma los números y los imprime. Llamamos a la función con diferentes cantidades de argumentos
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

# Llamamos a la función con diferentes cantidades de argumentos
suma(2, 5, 7)
suma(2, 8)
suma(2, 8, 9, 10)

