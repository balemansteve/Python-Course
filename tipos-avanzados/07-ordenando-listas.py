# Declaramos una lista de numeros
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Dos formas de ordenar una lista:

# Sort ordena la lista de menor a mayor, el parametro reverse=True la ordena de mayor a menor
numeros.sort(reverse=True)
print(numeros)

# Sorted crea una nueva lista ordenada de menor a mayor, el parametro reverse=True la ordena de mayor a menor
numeros2 = sorted(numeros, reverse=True)
print(numeros2)

# Declarar una lista de usuarios con su calificacion
usuarios = [["Bryan", 4], ["Juan", 2], ["Ana", 3], ["Carlos", 1]]

# Definir una funcion que regrese el segundo elemento de la sublista
def ordena(elemento):
    return elemento[1]

# Este algoritmo obtiene la calificacion del primer usuario mediante la funcion ordena
# primer_usuario = usuarios[0]
# calificacion = ordena(primer_usuario)
# print(calificacion)

# Ordenar la lista de usuarios de mayor a menor calificacion con la funcion ordena
# usuarios.sort(key=ordena, reverse=True)

# Ordenar la lista de usuarios de mayor a menor calificacion con una funcion lambda
usuarios.sort(key=lambda elemento: elemento[1], reverse=True)
print(usuarios)
