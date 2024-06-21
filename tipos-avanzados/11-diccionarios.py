# Son una coleccion de datos agrupados por una llave y un valor
# Solo acepta strings como llave, y el valor puede ser cualquier tipo de dato

punto = {"x": 25, "y": 50}
print(punto)

# Accedemos a los valores del diccionario
print(punto["x"])
print(punto["y"])

# Agregamos un nuevo valor al diccionario
punto["z"] = 45
print(punto)

# Intentar acceder a una llave que no se sabe si existe (para que no de error la aplicacion)
if "a" in punto:
    print(punto["a"])
    
# Otra forma de acceder a una llave que no se sabe si existe, si no existe retorna None
print(punto.get("a"))

# Otra forma de acceder a una llave que no se sabe si existe, si no existe retorna el valor que se le pase 
# sin modificar el diccionario
print(punto.get("a", 97))

print(punto)

# Eliminar un valor del diccionario
del punto["x"]
# Tambien existe una funcion para eliminar un valor del diccionario
del(punto["y"])

print(punto)

punto["x"] = 25
print(punto)

# Si iteramos un diccionario solo se iteran las llaves
for valor in punto:
    print(valor)
    
# Iteramos un diccionario y nos devuelve la llave y el valor agregando diccionario[valor]
for valor in punto:
    print(valor, punto[valor])
    
# Otra forma de acceder a los elementos de un diccionario
for valor in punto.items():
    print(valor)

# Desempaqueta los valores de un diccionario
for llave, valor in punto.items():
    print(llave, valor)
    
# Lista de diccionarios, se accede al valor de la llave elegida de cada diccionario
usuarios = [
    {"id": 1, "nombre": "Bryan"},
    {"id": 2, "nombre": "Nacho"},
    {"id": 3, "nombre": "Guille"},
    {"id": 4, "nombre": "Lucho"},
]

for usuario in usuarios:
    print(usuario["nombre"])
    
