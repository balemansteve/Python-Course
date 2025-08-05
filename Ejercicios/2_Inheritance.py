"""
Este módulo define una clase base 'Animal' y una subclase 'Dog'.
La clase 'Animal' tiene atributos comunes como 'name' y 'species',
y un método 'make_sound' que representa un sonido genérico.

La subclase 'Dog' hereda de 'Animal' y sobrescribe el método 'make_sound'
para emitir un sonido específico de perro.

Se crean instancias de ambas clases y se demuestra el uso del polimorfismo.
"""

class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def make_sound(self):
    print("Some generic sound")

class Dog(Animal):
  def __init__(self, name, species):
    super().__init__(name, species)
 
  def make_sound(self):
    print("Woof!")

animal = Animal("gato", "felino")
animal.make_sound()

dog = Dog("Perro", "Canino")
dog.make_sound()
