'''
JSON con Estructuras Anidadas
Serializar y deserializar objetos anidados como listas dentro de diccionarios.
'''

nested_data = {
    "employees": [
        {"name": "John", "age": 30},
        {"name": "Emma", "age": 25}
    ],
    "department": "HR"
}

# Serializar a JSON
with open("nested.json", "w") as jsonfile:
    json.dump(nested_data, jsonfile)

# Deserializar de JSON
with open("nested.json", "r") as jsonfile:
    loaded_nested_data = json.load(jsonfile)
    print(loaded_nested_data)
