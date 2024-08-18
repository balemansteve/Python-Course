# Definimos una funcion que recibe un texto y retorna su largo (cantidad de caracteres)
def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado 
    
    
print("chanchito")
l = largo("Hola Mundo")
print(l)