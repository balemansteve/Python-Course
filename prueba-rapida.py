nombres = ["Ale", "Bryan", "Maria"]
notas = [10, 8, 6]

ranking = []
for rank, (nombre, nota) in enumerate(zip(nombres, notas), start=1):
    ranking.append(f"{rank}. {nombre}: {nota}")
print(ranking)



# f"{rank}. {nombre}: {nota}"

