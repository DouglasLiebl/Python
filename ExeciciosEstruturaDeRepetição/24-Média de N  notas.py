# Faça um programa que calcule o mostre a média aritmética de N notas.

soma = 0
nNotas = 0
nota = 0
while nota != 'S':
    nota = input("Digite uma nota: ('S' para parar de inserir notas) ")
    if nota == 'S':
        break
    nNotas += 1
    soma = soma + float(nota)

media = soma / nNotas
print(f"A nota média é {media}")