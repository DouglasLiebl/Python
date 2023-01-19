# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

totalEleitores = int(input("Insira o número total de eleitores nesta sessão: "))
votosConcluidos = 0
candidato1 = 0
candidato2 = 0
candidato3 = 0
invalidos = 0
while votosConcluidos < totalEleitores:
    voto = input(" [1] Candidato 1 \n [2] Candidato 2 \n [3] Candidato 3 \nSelecione o candidato de preferência: ")
    if voto == '1':
        candidato1 += 1
    elif voto == '2':
        candidato2 += 1
    elif voto == '3':
        candidato3 += 1
    else:
        invalidos += 1
    votosConcluidos += 1

print(f"Votos totais: \n Candidato 1: {candidato1} \n Candidato 2: {candidato2} \n Candidato 3: {candidato3} \n Inválidos: {invalidos}")