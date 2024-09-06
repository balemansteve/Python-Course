# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2

comando = "" # Inicializar la variable comando

# Mientras el comando no sea "salir", imprimir el comando. lower() convierte el string a minúsculas para comparar con "salir" correctamentef
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)