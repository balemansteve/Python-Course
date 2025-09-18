"""
Ejemplo de función que calcula el largo de un texto:

- La función largo(texto) recorre cada carácter del string recibido y cuenta
  cuántos hay, incrementando 'resultado' en cada iteración.
- Devuelve el total de caracteres.
- Se imprime primero la palabra "chanchito" y luego el largo de "Hola Mundo"
  (que es 10, incluyendo el espacio).
"""

# Definimos una funcion que recibe un texto y retorna su largo (cantidad de caracteres)
def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado 
    
# Imprimimos el largo de un texto
print("chanchito")
l = largo("Hola Mundo")
print(l)

