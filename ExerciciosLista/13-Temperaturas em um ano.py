# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperaturas = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media = 0

for i in range(0, 12):
    temperaturas.append(float(input(f"Insira a temperatura média do mês de {meses[i]}: ")))
    media += temperaturas[i]

media /= 12
cont = 0 
print("\n")
while cont < len(meses):
    print(f"Temperatura média do mês de {meses[cont]}: {temperaturas[cont]:,.1f}°")
    cont += 1
print(f"\nTemperatura média do ano: {media:,.1f}°")