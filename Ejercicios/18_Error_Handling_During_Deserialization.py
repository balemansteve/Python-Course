'''
Tema: Manejo de Errores en Deserialización
Este ejercicio muestra cómo manejar datos corruptos o mal formateados durante la deserialización, usando try-except para evitar que el programa falle.

Tarea:
Intentar deserializar datos JSON mal formateados.
Manejar las excepciones con mensajes claros.
'''

import json

# JSON mal formado (falta una comilla de cierre para "name")
malformed_json = '{"name": "Alice", "age": 25, "city": "New York}'

try:
    # Intentamos deserializar el JSON
    data = json.loads(malformed_json)
    print(data)
except json.JSONDecodeError as e:
    # Manejo de errores en caso de JSON inválido
    print("Failed to deserialize JSON. Error:", e)
