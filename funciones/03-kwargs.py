# Definimos una función que recibe un número indeterminado de argumentos
def get_product(**datos):
    print(datos["id"], datos["nombre"])
    
# Llamamos a la función con diferentes cantidades de argumentos
get_product(id="23", nombre="iphone", precio="50")

