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

# Transformacion
# nombres = [expresion for i in items]
# nombres = [usuario[1] for usuario in usuarios]

# Filtramos
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# Filtrar y transformar
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
nombres.sort()
print(nombres)