'''
Herencia multiple: Permite que una clase herede atributos y métodos de múltiples clases.
'''
# Clase Flyable
class Flyable:
    def fly(self):
        print("I can fly!")

# Clase Swimmable
class Swimmable:
    def swim(self):
        print("I can swim!")

# Clase Duck que hereda de Flyable y Swimmable
class Duck(Flyable, Swimmable):
    pass  # No necesitamos añadir nada adicional

# Crear una instancia de Duck
duck = Duck()

# Llamar a los métodos heredados
duck.fly()
duck.swim()
