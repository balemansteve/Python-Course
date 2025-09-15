"""
Ejemplo de función con argumentos de palabra clave variables (**kwargs):

- La función get_product(**datos) recibe un número indeterminado de argumentos
  nombrados y los guarda en un diccionario llamado 'datos'.
- Se accede a valores específicos del diccionario usando sus claves,
  en este caso 'id' y 'nombre', y se imprimen.
- Al llamar la función, se pueden pasar más argumentos de los que la
  función utiliza (por ejemplo 'precio'), ya que quedan disponibles en el diccionario.
"""

# Definimos una función que recibe un número indeterminado de argumentos
def get_product(**datos):
    print(datos["id"], datos["nombre"])
    
# Llamamos a la función con diferentes cantidades de argumentos
get_product(id="23", nombre="iphone", precio="50")


