'''
Tema: Serializar Objetos Complejos
Los objetos como datetime no son serializables por defecto en JSON. Este ejercicio aborda cómo manejar este tipo de datos con codificadores y decodificadores personalizados.

Tarea:
Serializar un objeto que incluya datetime usando un codificador personalizado.
Deserializarlo de vuelta al objeto original con un decodificador personalizado.
'''

from datetime import datetime
import json

# Datos con datetime
data = {"event": "Meeting", "time": datetime.now()}

# Codificador personalizado
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            # Convertimos datetime a una cadena ISO 8601
            return obj.isoformat()
        return super().default(obj)

# Decodificador personalizado
def datetime_decoder(dct):
    if "time" in dct:
        # Convertimos la cadena ISO 8601 de vuelta a datetime
        dct["time"] = datetime.fromisoformat(dct["time"])
    return dct

# Serializar con el codificador personalizado
json_data = json.dumps(data, cls=DateTimeEncoder)
print("Serialized JSON:", json_data)

# Deserializar con el decodificador personalizado
deserialized_data = json.loads(json_data, object_hook=datetime_decoder)
print("Deserialized Data:", deserialized_data)
print("Event Time as datetime object:", deserialized_data["time"])
