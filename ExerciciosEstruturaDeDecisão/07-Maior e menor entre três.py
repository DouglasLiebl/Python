# Faça um Programa que leia três números e mostre o maior e o menor deles.

primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
terceiro = int(input("Digite o terceiro número: "))
maior = primeiro
menor = primeiro

if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro

print(f"O maior numero digitado é {maior} e o menor é {menor}")