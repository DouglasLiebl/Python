# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []
inversao = []

for i in range(0, 10):
    lista.append(float(input(f"Insira o número {i + 1}: ")))
    
cont = 9
for i in range(0, 10):
    inversao.append(lista[cont])
    cont -= 1

print(f"Números digitados: {lista} \nNúmeros invertidos: {inversao}")