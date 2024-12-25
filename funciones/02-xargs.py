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
