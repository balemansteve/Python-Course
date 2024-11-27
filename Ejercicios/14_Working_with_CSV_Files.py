'''
Los archivos CSV (Comma-Separated Values) se usan para almacenar datos tabulares.
'''

import csv  # Importar módulo CSV

# Crear el archivo CSV
with open("data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Escribir encabezados
    writer.writerow(["Name", "Age", "City"])
    # Escribir filas
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])
    writer.writerow(["Charlie", 35, "Chicago"])

# Leer y mostrar el archivo CSV
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print("\t".join(row))
