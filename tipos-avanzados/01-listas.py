# Declaramos varias listas con diferentes tipos de datos
numeros = [1, 2, 3]
letras = ["a", "b", "c"]
palabras = ["Hola", "Mundo", "Python"]
booleans = [True, False, True]
matriz = [[0, 1], [2, 3], [4, 5]]
ceros = [0] * 10
cero_y_uno = [0, 1] * 10

# Concatenamos listas
alfanumerico = numeros + letras

# funcion list() retorna una lista de un iterable

# funcion list() que toma el retorno de la funcion range() y lo convierte en una lista
rango = list(range(1, 11))
print(rango)

# funcion list() para convertir un string en una lista 
chars = list("hola mundo")
print(chars)
