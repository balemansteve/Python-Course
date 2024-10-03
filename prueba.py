# Definition of a class called Animal with two methods: run and sleep
class Animal:
    def __init__(self, nombre, edad):
        self.name = nombre
        self.age = edad
    
    def correr(self):
        print(f"{self.name} está corriendo")
        
    def dormir(self):
        print(f"{self.name} está durmiendo")
    pass

perro = Animal("Firulais, 10")

print(f"{perro.name} tiene {perro.age} años")
