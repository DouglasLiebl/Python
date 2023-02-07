# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = []
media = 0
nota = 0
for i in range(0, 10):
    print(f"Insira as notas do {i + 1}° aluno: ")
    for i in range(0, 4):
        nota = float(input(f"Insira a nota {i + 1}: "))
        media += nota
    if media / 4 >= 7.0:    
        medias.append(media / 4)
    media = 0
nAlunos = len(medias)
print(f"{nAlunos} de 10 alunos tiraram nota média maior ou igual a 7.0")