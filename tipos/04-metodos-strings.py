# Definimos una variable que almacena un string
animal = "  chanCHito feliz  "

# Imprimimos varios metodos que trabajan con strings (objeto.metodo())
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())
print(animal.strip())
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("cH"))
print(animal.replace("nCH", "j"))
print("nCH" in animal)
print("nCH" not in animal)