numeros = (1, 2, 3) + (4, 5 , 6)
print(numeros)

punto = tuple([1, 2])
print(punto)

menosNumeros = numeros[:2]
print(menosNumeros)

primero, segundo, *resto = numeros
print(primero, segundo, resto)

for i in numeros:
    print(i)

numerosList = list(numeros)
print(numerosList)