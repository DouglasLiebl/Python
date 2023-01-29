'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
'''

nomeA = input("Insira o nome do atleta: ")
saltos = []
cont = 0
maiorSalto = 0
menorSalto = 100 
media = 0
for i in range(0,5):
    saltos.append(float(input(f"Insira o valor do salto {i + 1}: ")))
    media += saltos[cont]
    if maiorSalto < saltos[cont]:
        maiorSalto = saltos[cont]
    if menorSalto > saltos[cont]:
        menorSalto = saltos[cont]
    cont += 1
media = (media - (maiorSalto + menorSalto)) / 3
print(f"\n\nAtleta: {nomeA} \n\nPrimeiro Salto: {saltos[0]} m \nSegundo Salto: {saltos[1]} m \nTerceiro Salto: {saltos[2]} m \nQuarto Salto: {saltos[3]} m \nQuinto Salto: {saltos[4]} m \n\nMelhor Salto: {maiorSalto} m \nPior Salto: {menorSalto} m \nMédia dos demais saltos: {media:,.2f} m \n\nResultado final: \n{nomeA}: {media:,.2f} m")