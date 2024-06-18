usuarios = [
    ["Bryan", 4], 
    ["Juan", 2], 
    ["Ana", 3], 
    ["Carlos", 1]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# nombres = [expresion for i in items]

# Transformacion - map
# nombres = [usuario[1] for usuario in usuarios]

# Filtramos - filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# Filtrar y transformar
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# Filtrar y transformar - con lambda usando la funcion map y filter
# nombres = list(map(lambda usuario: usuario[0], usuarios))

menosUsuario = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuario)

# print(nombres)