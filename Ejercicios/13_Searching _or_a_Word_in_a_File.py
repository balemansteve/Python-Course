'''
Este ejercicio demuestra cómo buscar palabras en un archivo y contar sus ocurrencias.
'''

# Pedir al usuario el nombre del archivo y la palabra
filename = input("Enter the filename: ")
search_word = input("Enter the word to search for: ")

# Contar ocurrencias
word_count = 0
try:
    with open(filename, "r") as file:
        for line in file:
            # Contar ocurrencias ignorando mayúsculas/minúsculas
            word_count += line.lower().count(search_word.lower())
    print(f"The word '{search_word}' appears {word_count} times in the file.")
except FileNotFoundError:
    print("The file does not exist.")
