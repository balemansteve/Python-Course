'''
Los atributos de clase son compartidos por todas las instancias de la clase, mientras que los atributos de instancia son específicos para cada objeto.
'''

# Clase Person
class Person:
    # Atributo de clase
    species = "Homo sapiens"

    def __init__(self, name, age):
        # Atributos de instancia
        self.name = name
        self.age = age

# Crear dos objetos de la clase Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Acceder a los atributos de instancia
print(f"{person1.name} is {person1.age} years old.")
print(f"{person2.name} is {person2.age} years old.")

# Acceder al atributo de clase
print(f"Species: {Person.species}")

# Cambiar el atributo de clase
Person.species = "Homo sapiens sapiens"
print(f"Updated Species: {Person.species}")

# Modificar atributos de instancia
person1.age = 31
print(f"{person1.name} is now {person1.age} years old.")
