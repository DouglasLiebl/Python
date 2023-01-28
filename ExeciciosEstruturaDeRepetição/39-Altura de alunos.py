# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

numAluno = []
altAluno = []
cont = 0

for i in range(0, 10):
    numAluno.append(int(input("Forneça o número do aluno: ")))
    altAluno.append(float(input("Forneça a altura do aluno: ")))
    
maiorAltura = numAluno[0]
menorAltura = altAluno[0]
nMaior, mMenor = 0, 0 
stop = 1

while stop < len(numAluno):
    if maiorAltura < altAluno[stop]:
        maiorAltura = altAluno[stop]
        mMaior = stop
    if menorAltura > altAluno[stop]:
        menorAltura = altAluno[stop]
        mMenor = stop
    stop += 1

print(f"Aluno mais alto: {numAluno[mMaior]}\n Altura: {maiorAltura / 100} \nAluno mais baixo: {numAluno[mMenor]}\n Altura: {menorAltura / 100}")