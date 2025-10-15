"""
Este programa demuestra el uso de varios métodos de cadenas (strings) en Python:

1. Se define una variable de tipo string con espacios y mezcla de mayúsculas y minúsculas.
2. Se aplican distintos métodos de cadena:
   - upper(), lower(): cambian el texto a mayúsculas o minúsculas.
   - strip(), lstrip(), rstrip(): eliminan espacios en blanco.
   - capitalize(), title(): modifican la capitalización del texto.
   - find(): busca una subcadena y devuelve su posición.
   - replace(): reemplaza parte del texto por otro valor.
   - in / not in: verifican si una subcadena está (o no) dentro del texto.

Finalmente, se imprimen los resultados de cada operación para observar los cambios en el string.
"""

# Definimos una variable que almacena un string
animal = "  chanCHito feliz  "

# Imprimimos varios metodos que trabajan con strings (objeto.metodo())
print(animal.upper()) # Convierte todos los caracteres del string a mayúsculas
print(animal.lower()) # Convierte todos los caracteres del string a minúsculas
print(animal.strip().capitalize()) # strip() Elimina los espacios en blanco al inicio y al final del string y capitalize() convierte la primera letra a mayúscula
print(animal.title()) # Convierte la primera letra de cada palabra a mayúscula
print(animal.strip()) # Elimina los espacios en blanco al inicio y al final del string
print(animal.lstrip()) # Elimina los espacios en blanco al inicio del string
print(animal.rstrip()) # Elimina los espacios en blanco al final del string
print(animal.find("cH")) # Encuentra la posición donde aparece "cH", o -1 si no lo encuentra
print(animal.replace("nCH", "j")) # Reemplaza "nCH" por "j" en el string
print("nCH" in animal) # Verifica si "nCH" está en el string y retorna True o False
print("nCH" not in animal) # Verifica si "nCH" no está en el string y retorna True o False

