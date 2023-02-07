# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

import math
numeros = []
somaQ = 0

for i in range(0, 10):
    numeros.append(int(input(f"Insira o {i + 1}° número: ")))
    somaQ += (math.pow(numeros[i], 2))

print(f"O números digitados foram: {numeros} \nA soma dos quadrados dos números digitados é: {somaQ:,.0f}")

