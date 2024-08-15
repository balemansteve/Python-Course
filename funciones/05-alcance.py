# Definimos una variable global
saludo = "Hola Python"

# Definimos una función que modifica la variable global
def saludar():
    global saludo
    saludo = "Hola Mundo"
    
# Definimos una función que no modifica la variable global
def saludaChanchito():
    saludo = "Hola Chanchito"

print(saludo)
saludar()
print(saludo)