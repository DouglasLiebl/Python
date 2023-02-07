#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

pares = []
impares = []
numeros = []

for i in range(0, 20):
    numeros.append(float(input(f"Insira o {i + 1}° número: ")))
    if int(numeros[i]) == numeros[i]:
        if numeros[i] % 2 == 0:
            pares.append(int(numeros[i]))
        else:
            impares.append(int(numeros[i]))
    else:
        numeros[i] = int(input("ERRO: Apenas números inteiros são permitidos \nInsira um número inteiro: "))
    numeros[i] = int(numeros[i])
print(f"Números digitados: {numeros} \nNúmeros pares digitados: {pares} \nNúmeros impares digitados: {impares}")

