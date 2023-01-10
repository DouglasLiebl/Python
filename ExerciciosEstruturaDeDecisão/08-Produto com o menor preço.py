# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Insira o preço do primeiro produto: "))
produto2 = float(input("Insira o preço do segundo produto: "))
produto3 = float(input("Insira o preço do terceiro produto: "))
cheapest = produto1

if produto2 < cheapest:
    cheapest = produto2
if produto3 < cheapest:
    cheapest = produto3

print(f"O produto a ser comprado deve ser o que custa R$ {cheapest}")