'''
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
'''

valoresSalarios = [range(200, 299), range(300, 399), range(400, 499), range(500, 599), range(600, 699), range(700, 799), range(800, 899), range(900, 999), range(1000,9999999)]
salarios = []
intervalos = ["R$200 - R$299 -> ", "R$300 - R$399 -> ", "R$400 - R$499 -> ", "R$500 - R$599 -> ", "R$600 - R$699 -> ", "R$700 - R$799 -> ", "R$800 - R$899 -> ","R$900 - R$999 -> ", "R$1000 em diante -> "]

nVendedores = int(input("Insira o número total de vendedores: "))
for i in range(0, nVendedores):
    vendasBrutas = float(input(f"Insira o valor total das vendas semanais do vendedor {i+1}: "))
    salario = 200 + (vendasBrutas * 0.09)
    salarios.append(round(salario))    
sorted(salarios, key = float)

classe = 0
cont = 0
stop = 0
print("Valor dos sálarios a serem pagos e sua quantidade:")
while cont < 9:
    while stop < nVendedores:   
        if salarios[stop] in valoresSalarios[cont]: 
            classe += 1
        stop += 1  
    stop = 0
    
    if classe > 0:
        print(intervalos[cont], classe)
        classe = 0
    
    cont += 1

'''
# Decidi fazer de uma forma na qual os intervalos sem vendedores não sao impresos, para imprimir todos intervalos seria assim:

while cont < 9:
    while stop < nVendedores:   
        if salarios[stop] in valoresSalarios[cont]: 
            classe += 1
        stop += 1  
    stop = 0
    print(intervalos[cont], classe)
    classe = 0
    
    cont += 1
'''
