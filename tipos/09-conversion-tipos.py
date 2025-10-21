"""
Este programa muestra cómo funciona la conversión de valores a tipo booleano (bool) en Python:

1. Se utiliza la función bool() para evaluar diferentes valores.
2. Reglas principales:
   - Cadenas vacías ("") → False
   - Cadenas con cualquier contenido, incluso "0" o espacios → True
   - El valor None (nulo) → False
   - El número 0 → False
   - Cualquier número distinto de 0 → True

Finalmente, se imprimen los resultados de cada conversión para observar el comportamiento de Python al evaluar la "verdad" de distintos valores.
"""

x = input("") # input devuelve un string

# int()
# str()
# float()
# bool()

print(bool("")) # imrpime False porque la cadena esta vacia
print(bool("0")) # imprime True porque la cadena tiene un 0
print(bool(None)) # imprime False porque None es un valor nulo
print(bool(" ")) # imprime True porque la cadena tiene un espacio
print(bool(0)) # imprime False porque el numero es 0
print(bool(1)) # imprime True porque el numero es 1

