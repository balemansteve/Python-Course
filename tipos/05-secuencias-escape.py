"""
Este programa muestra el uso de secuencias de escape en cadenas de texto (strings) en Python:

1. Las secuencias de escape permiten insertar caracteres especiales dentro de un string:
   - \"  → inserta una comilla doble.
   - \'  → inserta una comilla simple.
   - \\  → inserta una barra invertida.
   - \n  → representa un salto de línea.

2. Se define una cadena que incluye comillas dobles y un salto de línea usando estas secuencias.

Finalmente, se imprime el resultado mostrando cómo Python interpreta las secuencias de escape.
"""

# Secuencias de escape: Son combinaciones de caracteres que representan algo especial en un string, como saltos de línea o comillas.
# \" inserta una comilla doble dentro de un string
# \' inserta una comilla simple dentro de un string
# \\ inserta una barra invertida dentro de un string
# \n representa un salto de línea

# Definimos una variable que almacena un string con comillas dobles al principio y al final, y un salto de línea en el medio
curso = "\"Ultimate \nPython\""
print(curso)

