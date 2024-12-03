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
