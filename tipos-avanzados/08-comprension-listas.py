# Declaramos una lista de usuarios
usuarios = [
    ["Bryan", 4], 
    ["Juan", 2], 
    ["Ana", 3], 
    ["Carlos", 1]
]

# Declaramos una lista, con el metodo append vamos agregando el primer elemento de cada sublista
nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)

# nombres = [expresion for i in items]

# Transformacion - map

# Declaramos una lista, para cada sublista de la lista usuarios vamos guardando el segundo elemento en la lista creada
nombres = [usuario[1] for usuario in usuarios]
print(nombres)

# Filtramos - filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# Filtrar y transformar
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# Filtrar y transformar - con lambda usando la funcion map y filter
# nombres = list(map(lambda usuario: usuario[0], usuarios))

menosUsuario = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuario)

# print(nombres)