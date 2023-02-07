'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
-comprar apenas latas de 18 litros;
-comprar apenas galões de 3,6 litros;
-misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

area = float(input("Digite a área total a ser pintada: "))

litros = (area / 6)
round(litros+0.5)

#LATAS
latas = litros // 18
if latas % 18 != 0:
    latas += 1
precoLatas = latas * 80.00

#GALÕES
galoes = litros // 3.6
if galoes % 3.6 != 0:
    galoes += 1
precoGaloes = galoes * 25.00

#AMBOS JUNTOS
litros = litros * 1.10
round(litros+0.5)
latasM = litros // 18
galoesM = (litros % 18) / 3.6
if galoesM % 3.6 != 0:
    galoesM += 1
precoM = (latasM * 80.00) + (galoesM * 25.00)

print(f"Total de litros necessarios para pintura: {int(litros)} \n Apenas latas de 18 litros: {int(latas)} \n Preço total apenas latas: R$ {precoLatas:,.2f} \n Apenas galões de 3,6 litros: {int(galoes)} \n Preço total apenas galões: R$ {precoGaloes:,.2f} \n Latas e galões: \n Latas: {int(latasM)} \n Galões: {int(galoesM)} \n Preço total de latas e galões: R$ {precoM:,.2f}")


