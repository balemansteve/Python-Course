"""
Este programa muestra el uso de números y operadores aritméticos en Python:

1. Se declaran variables numéricas:
   - int (entero)
   - float (decimal)
   - complex (número imaginario, usando 'j' en lugar de 'i')

2. Se aplican operadores aritméticos sobre variables:
   - +=, -=, *=, /= para modificar el valor de una variable.

3. Se muestran ejemplos de operaciones básicas:
   - Suma (+)
   - Resta (-)
   - Multiplicación (*)
   - División (/) → devuelve un float
   - División entera (//) → devuelve solo la parte entera
   - Módulo (%) → devuelve el resto de una división
   - Potencia (**) → eleva un número a otro

Finalmente, se imprimen los resultados de las operaciones.
"""

numero = 2 # entero -> integer
decimal = 1.2 # float
imaginario = 2 + 2j # 2 + 2i -> j seria el numero imaginario

# Operadores aritméticos a variables
numero += 5 # numero = numero + 5
numero *= 5 # numero = numero * 5
numero -= 5 # numero = numero - 5
numero /= 5 # numero = numero / 5

print("numero", numero) 
print(1 + 3) # suma
print(1 - 3) # resta
print(1 * 3) # multiplicación
print(1 / 3) # división
print(1 // 3) # división entera
print(8 % 3) # módulo
print(2 ** 3) # potencia

