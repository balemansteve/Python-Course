'''
JSON Básico
1- Serializar un diccionario a un archivo JSON.
2- Leer el archivo y deserializarlo de nuevo.
'''

import json

# Diccionario de ejemplo
data = {"name": "Alice", "age": 25, "city": "New York"}

# Serializar y guardar en un archivo
with open("data.json", "w") as jsonfile:  # Convertimos el diccionario a JSON y lo guardamos usando json.dump.
    json.dump(data, jsonfile)

# Leer y deserializar el archivo
with open("data.json", "r") as jsonfile:  # Cargamos el JSON desde el archivo con json.load.
    loaded_data = json.load(jsonfile)
    print(loaded_data)
