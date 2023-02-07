# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
media = 0
cont = 0
for i in range(0, 4):
    notas.append(float(input(f"Insira a nota {i + 1}: ")))
    media += notas[cont]
    cont += 1
media /= 4

print(f"Notas do aluno: {notas} \nNota média: {media:,.1f}")
