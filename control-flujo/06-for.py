edad = 10

for numero in range(10):
    print(numero)
    if numero == edad:
        print("Edad encontrada", numero)
        break
else:
    print("Edad no encontrada")
    
for char in "Ultimate Python":
    print(char)