# Faça um Programa que leia três números e mostre o maior deles.

primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
terceiro = int(input("Digite o terceiro número: "))
maior = primeiro

if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

print(f"O maior número é: {maior}")