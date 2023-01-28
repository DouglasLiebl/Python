'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
'''

valor = float(input("Insira o valor da divida: "))
valorJuros = 0
valorParcela = 0
quantidadePar = 0
valorDivida = 0
juros = 0

print("Valor da Dívida  Valor dos Juros  Quantidade de Parcelas  Valor da Parcela")
for i in range(0, 13, 3):
    valorDivida = valor * (1 + (juros / 100))
    valorJuros = valorDivida - valor
    if i == 0:
        valorParcela = valorDivida / 1
    else:
        valorParcela = valorDivida / i
    if juros == 0:
        juros += 10
    else:
        juros += 5
    print(f"R$ {valorDivida:<13,.2f} {valorJuros:<16,.2f} {i:<23} R$ {valorParcela:>9,.2f}")