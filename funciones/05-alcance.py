saludo = "Hola Python"


def saludar():
    global saludo
    saludo = "Hola Mundo"
    
    
def saludaChanchito():
    saludo = "Hola Chanchito"

print(saludo)
saludar()
print(saludo)