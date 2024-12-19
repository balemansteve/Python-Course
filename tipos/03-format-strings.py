# Declaramos dos variables que son nombre y apellido
nombre = "Bryan"
apellido = "Aleman"

# Declaramos una variable que almacena mediante f string (cadena de formato) el indice 0 de la variable nombre y la suma de dos enteros
nombre_completo = f"{nombre[0]} {2 + 5}"
print(nombre_completo)

# Al almacenar una cadena con un entero la variable se convierte en un string
print(type(nombre_completo))
