# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

totalCDs = int(input("Insira o número total de CDs contidos na coleção: "))
media = 0
precoTotal = 0
for i in range(totalCDs):
    precoCD = float(input(f"Insira o valor do CD {i + 1}: "))
    precoTotal += precoCD
media = precoTotal / totalCDs
print(f"O valor total da coleção de CDs é de R$ {precoTotal:,.2f} e o preço médio por CD de R$ {media:,.2f}")
