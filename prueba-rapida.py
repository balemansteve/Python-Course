"""
Este módulo genera un ranking de estudiantes con sus respectivas notas.
Toma dos listas: una con nombres y otra con notas, y crea un listado 
ordenado con formato 'posición. nombre: nota'.
"""

nombres = ["Ale", "Bryan", "Maria"]
notas = [10, 8, 6]

ranking = []
for rank, (nombre, nota) in enumerate(zip(nombres, notas), start=1):
    ranking.append(f"{rank}. {nombre}: {nota}")
print(ranking)


# f"{rank}. {nombre}: {nota}"
