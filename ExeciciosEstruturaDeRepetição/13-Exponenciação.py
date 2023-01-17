# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Digite um número: "))
expoente = int(input("Digite mais um número: "))

produto = base
cont = 1
while cont < expoente:
    produto = produto * base
    cont += 1

print(f"O produto de {base} elevado a {expoente}ª potência é {produto}")