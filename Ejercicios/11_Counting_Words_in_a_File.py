'''
Este ejercicio utiliza lectura de archivos y manipulación de cadenas para contar palabras.
'''

# Crear el archivo con texto
with open("words.txt", "w") as file:
    file.write("Python is fun.\n")
    file.write("File handling is easy in Python.\n")

# Leer el archivo y contar palabras
word_count = 0
with open("words.txt", "r") as file:
    for line in file:
        # Dividir la línea en palabras y sumar al contador
        words = line.split()
        word_count += len(words)

print(f"Total words: {word_count}")
