# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = int(input("Digite o tamanho do conjunto: "))
conjunto = []
soma = 0
for i in range(1, n + 1):
    conjunto.append(int(input("Forneça um número: ")))

cont = 1
maiorNumero = conjunto[0]
menorNumero = conjunto[0]
soma = conjunto[0]
while cont < len(conjunto):
    if maiorNumero < conjunto[cont]:
        maiorNumero = conjunto[cont]
    if menorNumero > conjunto[cont]:
        menorNumero = conjunto[cont]
    soma = soma + conjunto[cont]
    cont += 1
    
print(f"O maior número do conjunto é {maiorNumero}, o menor é {menorNumero} e a soma de todos o números é {soma}")