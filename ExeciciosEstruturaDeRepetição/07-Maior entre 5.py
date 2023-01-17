# Faça um programa que leia 5 números e informe o maior número.

numero = []
for i in range(1, 6):
    numero.append(int(input("Digite um número: ")))

maiorN = 0
contador = 1
while contador < len(numero):
    if numero[contador] > maiorN:
        maiorN = numero[contador]
    contador += 1

print(f"O maior número digitado é {maiorN}")