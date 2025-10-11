"""
Este programa demuestra conceptos básicos sobre variables en Python:

1. Python distingue entre mayúsculas y minúsculas (case-sensitive):
   - Variables con nombres similares pero diferentes en mayúsculas/minúsculas se consideran distintas.

2. Se definen variables con distintos tipos de datos:
   - str (cadena de texto)
   - int (entero)
   - float (decimal)
   - bool (booleano)

3. Se utilizan las funciones print() y type() para mostrar los valores y sus tipos de datos.
"""

# Definimos variables con distintas semánticas en sus nombres, mostrando que Python es case-sensitive (distingue minusculas de mayusculas)
nombre_curso = "Ultimate Python"
nombre1 = "Ultimate Python"
noMbre_curso = "Mundo"

# Imprimimos dos variables para mostrar el case-sentitive
print(nombre_curso, noMbre_curso)

# Definimos variables con distintos tipos de datos, int, float y bool
alumnos = 5000
puntaje = 9.9
publicado = True

# Imprimimos las variables y sus tipos de datos usando la funcion inegrada type()
print(type(alumnos), type(puntaje), type(publicado))

