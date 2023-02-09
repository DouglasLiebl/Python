# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetorA = []
vetorB = []
vetorC = []
vetoresConcluidos = 0


for i in range(0, 10):
    vetorA.append(input(f"Insira o {i + 1}° elemento do vetor A: "))
for i in range(0, 10):
    vetorB.append(input(f"Insira o {i + 1}° elemento do vetor B: "))

cont = 0
while cont < len(vetorA):
    vetorC.append(vetorA[cont])
    vetorC.append(vetorB[cont])
    cont += 1

print(f"Vetor A: {vetorA} \nVetor B: {vetorB} \nVetor C composto pelos elementos dos vetores A e B intercalados: {vetorC}")