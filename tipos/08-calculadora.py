"""
Este programa es una calculadora simple que:

1. Solicita al usuario ingresar dos números mediante input().
   - Los valores ingresados se reciben como strings.
2. Convierte los valores a enteros usando int().
3. Realiza las cuatro operaciones básicas:
   - Suma (+)
   - Resta (-)
   - Multiplicación (*)
   - División (/)
4. Usa una f-string con comillas triples para mostrar los resultados en varias líneas.

Finalmente, imprime los resultados de las operaciones de manera ordenada y legible.
"""

# Description: Calculadora simple que recibe dos numeros y muestra la suma, resta, multiplicacion y division de los mismos

n1 = input("Ingresa primer numero") # input devuelve un string
n2 = input("Ingresa segundo numero") # input devuelve un string

n1 = int(n1) # Convertimos el string a entero
n2 = int(n2) # Convertimos el string a entero

suma = n1 + n2 # Sumamos los dos numeros
resta = n1 - n2 # Restamos los dos numeros
multi = n1 * n2 # Multiplicamos los dos numeros
div = n1 / n2 # Dividimos los dos numeros

# Usamos f-string para mostrar el mensaje, se usan comillas triples ("""mensaje""") para poder escribir en varias lineas 
mensaje = f""" 
Para los numeros {n1} y {n2}.
el resultado de suma es {suma}.
el resultado de resta es {resta}.
el resultado de multiplicacion es {multi}.
el resultado de division es {div}.
"""

print(mensaje)

