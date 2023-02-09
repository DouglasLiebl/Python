#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetorA = []
vetorB = []
vetorC = []
vetorD = []

for i in range(0, 10):
    vetorA.append(input(f"Insira o {i + 1}° elemento do vetor A: "))
    vetorB.append(input(f"Insira o {i + 1}° elemento do vetor B: "))
    vetorC.append(input(f"Insira o {i + 1}° elemento do vetor C: "))
    # Fiz assim para ficar diferente do anterior xD

cont = 0
while cont < len(vetorA):
    vetorD.append(vetorA[cont])
    vetorD.append(vetorB[cont])
    vetorD.append(vetorC[cont])
    cont += 1

print(f"Vetor A: {vetorA} \nVetor B: {vetorB} \nVetor C: {vetorC} \nVetor D contendo, de forma intercalada, os vetores A, B e C: {vetorD}")