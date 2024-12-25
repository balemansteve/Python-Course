# Crea una tupla a partir de la concatenacion de dos tuplas
numeros = (1, 2, 3) + (4, 5 , 6)
print(numeros)

# Crea una tupla a partir de una lista
punto = tuple([1, 2])
print(punto)

# Crea una tupla con los dos primeros elementos de otra tupla
menosNumeros = numeros[:2]
print(menosNumeros)

# Crea tres variables a partir de una tupla
primero, segundo, *resto = numeros
print(primero, segundo, resto)

# Itera sobre una tupla
for i in numeros:
    print(i)

# Crea una lista a partir de una tupla
numerosList = list(numeros)
print(numerosList)