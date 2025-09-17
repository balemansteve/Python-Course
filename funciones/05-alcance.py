"""
Ejemplo de variable global y su modificación dentro de funciones:

- Se define una variable global 'saludo' con el valor "Hola Python".
- La función saludar() usa la palabra clave 'global' para indicar que
  modificará la variable global, cambiando su valor a "Hola Mundo".
- La función saludaChanchito() crea una variable local llamada 'saludo'
  (diferente de la global) y no afecta el valor global.
- En la ejecución:
    1. Se imprime la variable global ("Hola Python").
    2. Se llama a saludar(), que cambia la variable global.
    3. Se imprime de nuevo mostrando el nuevo valor ("Hola Mundo").
"""

# Definimos una variable global
saludo = "Hola Python"

# Definimos una función que modifica la variable global
def saludar():
    global saludo
    saludo = "Hola Mundo"
    
# Definimos una función que no modifica la variable global
def saludaChanchito():
    saludo = "Hola Chanchito"

# Primero imprimimos la variable global, luego la modificamos y volvemos a imprimirla pero no se imprime el cambio
print(saludo)
saludar()
print(saludo)

