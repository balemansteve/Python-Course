'''
Este ejercicio demuestra cómo leer un archivo y escribir su contenido en otro archivo.
'''

# Crear el archivo fuente
with open("source.txt", "w") as source:
    source.write("This is the source file.\nIt contains some text.\n")

# Copiar el contenido al archivo destino
with open("source.txt", "r") as source:
    with open("destination.txt", "w") as destination:
        for line in source:
            destination.write(line)

print("File copied successfully")
