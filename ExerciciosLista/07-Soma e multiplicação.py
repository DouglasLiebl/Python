# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros = []
soma = 0
multiplicacao = 1

for i in range(0, 5):
    numeros.append(int(input(f"Insira o {i + 1}° número: ")))
    soma += numeros[i]
    multiplicacao *= numeros[i]

print(f"Números digitados: {numeros} \nSoma de todos números digitados: {soma} \nMultiplicação de todos números digitados: {multiplicacao}")