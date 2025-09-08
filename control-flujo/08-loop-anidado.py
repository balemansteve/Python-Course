"""
Ejemplo de bucle anidado:
- El bucle externo (j en range(3)) controla las filas → valores 0, 1 y 2.
- El bucle interno (k en range(2)) controla las columnas → valores 0 y 1.
- Por cada valor de j, se recorren todos los valores de k y se imprimen las parejas (j, k).
"""

# Bucle anidado es un bucle dentro de otro bucle, primero se ejecuta el bucle interno y luego vuelva a ejecutar el bucle externo
for j in range(3):
    for k in range(2):
        print(f"{j}, {k}")

