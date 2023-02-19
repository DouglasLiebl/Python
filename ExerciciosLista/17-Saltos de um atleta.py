'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''

saltos = []
ordemSaltos = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
media = 0
atleta = input("Insira o nome do atleta: ")
while atleta == "":
    atleta = input("ERRO: Insira o nome do atleta para continuar: ")
for i in range(0, 5):
    saltos.append(float(input(f"{ordemSaltos[i]} salto: ")))
    media += saltos[i]
media /= 5

print(f"\nResultado final: \nAtleta: {atleta} \nSaltos: {saltos[0]} - {saltos[1]} - {saltos[2]} - {saltos[3]} - {saltos[4]} \nMédia dos saltos: {media:,.1f} m")
