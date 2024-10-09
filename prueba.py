# Definition of a class called Animal with two atributtes and two methods
class Animal:
    # Constructor of the class Animal
    def __init__(self, nombre, edad):
        self.name = nombre
        self.age = edad
    
    # Methods of the class Animal
    def correr(self):
        print(f"{self.name} está corriendo")
        
    def dormir(self):
        print(f"{self.name} está durmiendo")
    pass

# Create an object of the class Animal
perro = Animal("Firulais, 10")

# Call the methods of the object perro
print(f"{perro.name} tiene {perro.age} años")
