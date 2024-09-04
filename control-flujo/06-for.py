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