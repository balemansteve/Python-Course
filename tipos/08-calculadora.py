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
