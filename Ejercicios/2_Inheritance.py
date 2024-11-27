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
