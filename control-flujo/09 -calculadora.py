"""
Programa que simula una calculadora básica en consola.

- El usuario ingresa un número inicial, una operación y luego otro número.
- Se pueden realizar las operaciones: suma, resta, multi y div.
- El resultado se va actualizando después de cada operación.
- El programa funciona en un bucle infinito hasta que el usuario escriba "salir"
  en cualquiera de las entradas (número, operación o segundo número).
- Si el usuario escribe una operación no válida, se muestra un mensaje y el 
  programa finaliza.
"""

# Programa que simula una calculadora, donde el usuario ingresa un número, una operación y otro número, y el programa muestra el resultado de la operación
# El programa se ejecuta en un bucle infinito hasta que el usuario ingresa la palabra "salir"
print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    operador = input("Ingrese la operación: ")
    if operador.lower() == "salir":
        break
    num2 = input("Ingrese el siguiente número: ")
    if num2.lower() == "salir":
        break
    num2 = int(num2)
    
    if operador == "suma":
        resultado += num2
    elif operador == "resta":
        resultado -= num2
    elif operador == "multi":
        resultado *= num2
    elif operador == "div":
        resultado /= num2
    else:
        print("Operacion no valida")
        break
    
    print(f"El resultado es {resultado}")

