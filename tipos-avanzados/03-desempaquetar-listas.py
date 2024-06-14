numeros = [1, 2, 3, 4, 5]

# feo!
# primero = [0]
# segundo = [1]
# tercero = [2]

# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

primero, *otros, penu, ultimo = numeros
print(primero, penu, ultimo)
print(otros)
