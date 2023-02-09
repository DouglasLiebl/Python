# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = []
altura = []
media = 0
alunosInfM = 0

for i in range(0, 30):
    idades.append(int(input(f"Insira a idade do aluno {i + 1}: ")))
    altura.append(int(input(f"Insira a altura do aluno {i + 1}, em cm: ")))
    media += altura[i]
media /= 30
cont = 0

while cont < 30:
    if altura[cont] < media and idades[cont] > 13:
        alunosInfM += 1
    cont +=1
print(f"Média de altura dos alunos: {media:,.0f} cm \nNúmero de alunos com mais de 13 anos e altura inferior à média: {alunosInfM}")