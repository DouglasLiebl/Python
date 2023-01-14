'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
-par ou ímpar;
-positivo ou negativo;
-inteiro ou decimal.
'''

def parImpar(n):
    n = n % 2

    if n == 0:
        return "Par"
    else:
        return "Impar"

def positivoNegativo(n):
    if n > 0:
        return "Positivo"
    if n < 0:
        return "Negativo"

def inteiroDecimal(n):
    if n == round(n):
        return "Inteiro"
    else:
        return "Decimal"

n1 = float(input("Insira o primeiro valor: "))
n2 = float(input("Insira o valor do segundo valor: "))
operador = input("Qual operação deseja realizar? ")

match operador:
    case 'soma':
        operacao = n1 + n2
    case 'subtração':
        operacao = n1 - n2
    case 'divisão':
        operacao = n1 / n2
    case 'multiplicação':
        operacao = n1 * n2

print (f"O resultado da operação desejada é {operacao}, este resultado é um número {inteiroDecimal(operacao)}, {positivoNegativo(operacao)} e {parImpar(operacao)}")