"""
Este programa muestra cómo trabajar con cadenas de texto (strings) en Python:

1. Se crean variables tipo string, incluyendo una con múltiples líneas usando triple comillas.
2. Se realizan operaciones comunes sobre cadenas:
   - Obtener la longitud con len().
   - Acceder a caracteres individuales mediante índices.
   - Extraer porciones (slicing) de texto usando rangos.
3. Se imprime una cadena multilínea para mostrar cómo conserva los saltos de línea.

Finalmente, se imprimen los resultados de cada operación.
"""

# Definimos una variable tipo string
nombre_curso = "Ultimate Python"

# Definimos una variable tipo string con saltos de linea (agregando """ al inicio y al final)
descripcion_curso = """Ultimate Python, este curso contempla todo lo que necesitas 
saber para trabajar como programador"""

# Realizamos varios tipos de impresiones de la variable nombre_curso
print(len(nombre_curso))
print(nombre_curso[0])
print(nombre_curso[0:8])
print(nombre_curso[9:])
print(nombre_curso[:8])
print(nombre_curso[:])

# Imprimimos la variable descripcion_curso y se pueden ver los saltos de linea
print(descripcion_curso)

