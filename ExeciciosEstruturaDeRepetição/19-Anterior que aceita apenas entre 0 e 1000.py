# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n = int(input("Digite o tamanho do conjunto: "))
conjunto = []
for i in range(1, n + 1):
    conjunto.append(int(input("Forneça um número: ")))
    if conjunto[0] < 0 or conjunto[0] > 1000:
        print("ERRO: São aceitos apenas números entre 0 e 1000")

cont = 1
maiorNumero, menorNumero, soma = conjunto[0]
while cont < len(conjunto):
    if maiorNumero < conjunto[cont]:
        maiorNumero = conjunto[cont]
    if menorNumero > conjunto[cont]:
        menorNumero = conjunto[cont]
    soma += conjunto[cont]
    cont += 1

print(f"O maior número do conjunto é {maiorNumero}, o menor é {menorNumero} e a soma é {soma}")
    