"""
Ejemplo de bucles while:

1. (Comentado) Un ciclo que imprime el valor de 'numero' y lo multiplica por 2
   en cada iteración, mientras sea menor que 100.

2. Se inicializa la variable 'comando' como cadena vacía.
   Luego, con un ciclo while, se pide al usuario que ingrese texto hasta que 
   escriba "salir".
   - Se usa .lower() para convertir la entrada a minúsculas y evitar problemas 
     al comparar.
   - Cada vez que el usuario ingresa un comando, este se imprime en pantalla.
"""

# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2

comando = "" # Inicializar la variable comando

# Mientras el comando no sea "salir", imprimir el comando. lower() convierte el string a minúsculas para comparar con "salir" correctamente
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

