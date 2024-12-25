# set significa grupo o conjunto
# solo hay una instancia de cada elemento
primer = {1, 1, 2, 3, 4}
# primer.add(5)
# # primer.remove(1)
print(primer)

# Crea un set a partir de una lista
segundo = [3, 4, 5]
segundo = set(segundo)
print(segundo)

# Imprime la union de los dos sets (operador union '|')
print(primer | segundo)

# imprime la interseccion de los dos sets (operador interseccion '&')
# son los elementos que estan en ambos sets
print(primer & segundo)

# imprime la diferencia de los dos sets (operador diferencia '-')
# son los elementos que estan en el primer set pero no en el segundo, es decir que quita del primer set los elementos que esten en el segundo
print(primer - segundo)

# imprime la diferencia simetrica de los dos sets (operador diferencia simetrica '^')
# son los elementos que no se repiten en ambos sets
print (primer ^ segundo)