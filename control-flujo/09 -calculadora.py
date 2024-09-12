# Programa que simula una calculadora, donde el usuario ingresa un numero, una operacion y otro numero, y el programa muestra el resultado de la operacion
# El programa se ejecuta en un bucle infinito hasta que el usuario ingresa la palabra "salir"
print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    operador = input("Ingrese la operacion: ")
    if operador.lower() == "salir":
        break
    num2 = input("Ingrese el siguiente numero: ")
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
    
    



