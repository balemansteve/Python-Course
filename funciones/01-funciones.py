"""
Ejemplo de función con argumentos por defecto y argumentos nombrados:

- Se define la función hola(nombre, apellido="Feliz"):
  - 'apellido' tiene un valor por defecto ("Feliz") si no se pasa como argumento.
  - La función imprime un mensaje de bienvenida con el nombre y el apellido.

- Se llama a la función de tres maneras:
  1. Con dos argumentos → el segundo sobrescribe el valor por defecto.
  2. Con un solo argumento → el apellido toma el valor por defecto.
  3. Con argumentos nombrados → se pueden pasar en cualquier orden.
"""

# Definir una función que reciba un nombre y un apellido, y que imprima un mensaje de bienvenida. El apellido debe tener un valor por defecto de "Feliz". Llamar a la función con un solo argumento y con dos argumentos
def hola(nombre, apellido="Feliz"):
    print("Hola, mundo!")
    print(f"Bienvenido {nombre} {apellido}")

# Llamar a la función con dos argumentos, el segundo sobreescribe el valor por defecto
hola("Bryan", "Aleman")

# Llamar a la funcion con un solo argumento, el segundo toma el valor por defecto
hola("Ombligo")

# Llamar a la funcion con argumentos nombrados, aunque no se respete el orden, se asignan a los argumentos correspondientes
hola(apellido="Aleman", nombre="Bryan")

