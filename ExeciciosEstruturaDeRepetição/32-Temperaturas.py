# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.


conjuntoTemp = []
temperatura = 0
soma = 0
media = 0
print("Digite 'S' para sair")

while temperatura != 'S':
    temperatura = (input("Insira o valor da temperatura: "))
    soma = soma + temperatura
    media += 1  
    if temperatura == 'S':
        break
    conjuntoTemp.append(float(temperatura))

media = soma / media
maiorTemperatura = conjuntoTemp[0]
menorTemperatura = conjuntoTemp[0]
cont = 1

while cont < len(conjuntoTemp):
    if conjuntoTemp[cont] > maiorTemperatura:
        maiorTemperatura = conjuntoTemp[cont]
    if conjuntoTemp[cont] < menorTemperatura:
        menorTemperatura = conjuntoTemp[cont]
    cont += 1

print(f"A maior temperatura registrada foi {maiorTemperatura}° \nA menor temperatura registrada foi {menorTemperatura}° \nA média das temperaturas registradas foi {media}")