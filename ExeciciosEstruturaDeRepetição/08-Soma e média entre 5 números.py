# Faça um programa que leia 5 números e informe a soma e a média dos números.

numero = []
for i in range(1, 6):
    numero.append(int(input("Digite um número: ")))

soma = numero[0]
cont = 1
while cont < len(numero):
    soma = soma + numero[cont]
    cont += 1

media = soma / 5
print(f"A soma de todos números digitados é {soma:,.0f} e a média entre eles é {media}")