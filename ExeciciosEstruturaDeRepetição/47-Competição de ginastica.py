'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04

'''

atleta = input("Insira o nome do atleta: ")
notas = []
melhorNota = 0
menorNota = 100
cont = 0
media = 0
for i in range(0, 7):
    notas.append(float(input(f"Insira a nota {i + 1}: ")))
    if melhorNota < notas[cont]:
        melhorNota = notas[cont]
    if menorNota > notas[cont]:
        menorNota = notas[cont]
    media += notas[cont]
    cont += 1
media = (media - (melhorNota + menorNota)) / 5
cont = 0
while cont < len(notas):
    print(f"Nota {cont + 1}: {notas[cont]}")
    cont += 1
print(f"\nResultado final: \nAtleta: {atleta} \nMelhor nota: {melhorNota} \nPior nota: {menorNota} \nMédia: {media:,.2f}")