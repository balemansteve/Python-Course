# Escribir en el archivo
with open("example.txt", "w") as file:
    # Escribimos las líneas en el archivo
    file.write("Hello, world!\n")
    file.write("Welcome to file I/O in Python.\n")

# Leer del archivo
with open("example.txt", "r") as file:
    # Leer línea por línea e imprimir
    for line in file:
        print(line.strip())
