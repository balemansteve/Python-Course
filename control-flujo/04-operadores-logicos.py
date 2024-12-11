# and, or, not
# and: si ambos valores son True, devuelve True
# or: si al menos uno de los valores es True, devuelve True
# not: invierte el valor booleano

gas = False
encendido = True
edad = 15

if not gas or (encendido and edad > 17):
    print("Puedes avanzar")
