"""
Se utiliza un operador ternario para asignar un valor a la variable 'mensaje'.
El operador ternario evalúa la condición 'edad > 17':
    - Si es True, asigna "Es mayor"
    - Si es False, asigna "Es menor"
Esta forma es equivalente al bloque if-else comentado más abajo.
"""

edad = 15

# El operador ternario es una forma de simplificar un if-else, 
donde se evalúa una condición y se asigna un valor si es verdadera y otro si es falsa
mensaje = "Es mayor" if edad > 17 else "Es menor"

# if edad > 17:
#     mensaje = "Es mayor"
# else:
#     mensaje = "Es menor"
    
print(mensaje)


