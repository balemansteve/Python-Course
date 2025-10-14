"""
Este programa muestra cómo usar f-strings (cadenas de formato) en Python:

1. Se declaran variables con nombre y apellido.
2. Se crea una nueva cadena usando una f-string que:
   - Accede a un carácter específico dentro de una variable (nombre[0]).
   - Realiza operaciones dentro de la cadena (2 + 5).
3. Se imprime el resultado y se verifica su tipo de dato con type(),
   mostrando que una f-string siempre produce una cadena (string).
"""

# Declaramos dos variables que son nombre y apellido
nombre = "Bryan"
apellido = "Aleman"

# Declaramos una variable que almacena mediante f string (cadena de formato) el indice 0 de la variable nombre y la suma de dos enteros
nombre_completo = f"{nombre[0]} {2 + 5}"
print(nombre_completo)

# Al almacenar una cadena con un entero la variable se convierte en un string
print(type(nombre_completo))

