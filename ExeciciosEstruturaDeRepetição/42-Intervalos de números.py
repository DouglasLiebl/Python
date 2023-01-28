# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

n = 0
limite25 = 0
limite50 = 0
limite75 = 0
limite100 = 0

while n >= 0 and n < 101:
    n = int(input("Insira um número positivo inteiro: "))
    if n >= 0 and n < 26:
        limite25 += 1
    elif n > 25 and n < 51:
        limite50 += 1
    elif n > 50 and n < 76:
        limite75 += 1
    elif n > 75 and n <101:
        limite100 += 1

print(f"Números no intervalo [0-25]: {limite25} \nNúmeros no intervalo [26-50]: {limite50} \nNúmeros no intervalo [51-75]: {limite75} \nNúmeros no intervalo [76-100]: {limite100}")