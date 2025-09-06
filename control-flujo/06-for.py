"""
Ejemplo de uso de bucles for:
1. Se recorre una secuencia de números generada con range(10), 
   que produce valores de 0 a 9.
   - En cada iteración se imprime el número.
   - Si el número coincide con la variable 'edad', se imprime 
     "Edad encontrada" y se interrumpe el ciclo con break.
   - Si el ciclo termina sin encontrar la edad, se ejecuta el bloque 'else'.
2. Luego, se recorre un string ("Ultimate Python") e imprime cada carácter.
"""

edad = 10

# Iterar sobre una lista de números y comparar con la edad, si la edad es encontrada, imprimir un mensaje y salir del ciclo con break
# range() genera una lista de números desde 0, la cantidad de números es el argumento que se le pasa
for numero in range(10):
    print(numero)
    if numero == edad:
        print("Edad encontrada", numero)
        break
else:
    print("Edad no encontrada")

# Iterar sobre un string e imprimir cada caracter
for char in "Ultimate Python":
    print(char)

