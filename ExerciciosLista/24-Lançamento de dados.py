'''
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
'''

from random import randint

def randomizador():
    random = (randint(1, 6))
    return random

resultados = []
vezes_resultado = [0, 0, 0, 0, 0, 0]

for i in range(0, 100):
    resultados.append(randomizador())
    vezes_resultado[resultados[i] - 1] += 1
    if i == 99:
        print(f"Números sorteados: \n{resultados}")
        stop = 0
        while stop < len(vezes_resultado):
            print(f"Número {stop + 1}: {vezes_resultado[stop]} vezes sorteado")
            stop += 1