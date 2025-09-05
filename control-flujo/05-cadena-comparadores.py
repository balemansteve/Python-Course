"""
Ejemplo de comparadores en cadena.
La condición '15 <= edad <= 65' se lee como:
    - edad >= 15 y edad <= 65
Si la condición se cumple, imprime que puede entrar a la piscina.
Esto hace el código más compacto y legible que escribir dos comparaciones separadas.
"""

# Comparadores en cadena
edad = 25
if 15 <= edad <= 65:
    print("Puede entrar a la piscina")

