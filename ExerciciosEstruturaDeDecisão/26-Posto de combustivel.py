'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
-Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
-Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 
 Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

tipoC = input("Selecione o tipo de combustível: \n [A] Álcool \n [G] Gasolina \n Escolha: ")
litros = float(input("Agora insira a quantidade de litros desejada: "))

match tipoC:
    case 'A':
        if litros < 20:
            preco = litros * 1.90
            preco = preco * 0.97
        else: 
            preco = litros * 1.90
            preco = preco * 0.95
        
        print(f"{litros} litros de Álcool terá o custo de R$ {preco:,.2f}")
    case 'G':
        if litros < 20:
            preco = litros * 2.50
            preco = preco * 0.96
        else:
            preco = litros * 2.50
            preco = preco * 0.94
        
        print(f"{litros} litros de Gasolina terá o custo de R$ {preco:,.2f}")