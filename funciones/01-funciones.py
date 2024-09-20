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
