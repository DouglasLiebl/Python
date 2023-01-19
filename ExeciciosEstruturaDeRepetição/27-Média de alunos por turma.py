#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

nTurmas = int(input("Forneça o número total de turmas: "))
media = 0
totalAlunos = 0
for i in range(nTurmas):
    alunos = int(input(f"Digite o número de alunos para a turma {i + 1}: "))
    if alunos > 40:
        alunos = int(input(f"As turmas não podem ter mais de 40 alunos \nDigite o número de alunos para a turma {i + 1}: "))
    totalAlunos += alunos
media = (totalAlunos // nTurmas) + 1
print(f"A média é de {media} alunos por turma")
