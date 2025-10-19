"""
Este programa muestra cómo usar funciones matemáticas integradas en Python y del módulo math:

1. Funciones integradas:
   - round(): redondea un número al entero más cercano.
   - abs(): devuelve el valor absoluto de un número.

2. Funciones del módulo math:
   - math.ceil(): redondea hacia arriba al entero más próximo.
   - math.floor(): redondea hacia abajo al entero más próximo.
   - math.pow(base, exponente): calcula una potencia.
   - math.sqrt(): calcula la raíz cuadrada de un número.
   - math.isnan(): verifica si un valor no es un número (comentado en el ejemplo).

Finalmente, se imprimen los resultados de cada operación para observar su comportamiento.
"""

import math # Importamos la librería math (tiene funciones matemáticas)

print(round(1.3)) # Redondea al entero más cercano
print(round(1.7))
print(round(1.5))
print(abs(55)) # Valor absoluto

print(math.ceil(1.1)) # Redondea al entero más grande
print(math.floor(1.9999)) # Redondea al entero más pequeño
#print(math.isnan("23")) # No es un número
print(math.pow(10, 3)) # Potencia pow(base, exponente)
print(math.sqrt(9)) # Raíz cuadradad

