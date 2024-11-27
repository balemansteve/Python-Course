'''
Usar pickle para guardar y cargar objetos Python.
'''

import pickle

# Clase personalizada
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# Crear un objeto
person = Person("Alice", 25)

# Serializar con pickle
with open("person.pkl", "wb") as picklefile:
    pickle.dump(person, picklefile)

# Deserializar con pickle
with open("person.pkl", "rb") as picklefile:
    loaded_person = pickle.load(picklefile)
    print(loaded_person)
