# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input("Insira a área total, em metros quadrados, a ser pintada: "))



litros = area / 3
latas = litros // 18
resto = litros % 18
latas = int(latas)
if resto > 0:
    latas += 1

preco = latas * 80.00

print(f"Serão necessarias {latas} latas de tinta e o valor total é de R$ {preco:,.2f}")

