numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [["Bryan", 4], ["Juan", 2], ["Ana", 3], ["Carlos", 1]]


# def ordena(elemento):
#     return elemento[1]


# usuarios.sort(key=ordena, reverse=True)
usuarios.sort(key=lambda elemento: elemento[1], reverse=True)
print(usuarios)