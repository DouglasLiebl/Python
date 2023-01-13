'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
-Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
-Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

valor = int(input("Insira a quantidade que deseja sacar: (max: 600/min: 10) "))

nota100 = valor // 100
resto100 = valor % 100
nota50 = resto100 // 50
resto50 = resto100 % 50
nota10 = resto50 // 10
resto10 = resto50 % 10
nota5 = resto10 // 5
resto5 = resto10 % 5
nota1 = resto5

print("Você receberá: ")
if nota100 == 1:
    print("1 Nota de R$ 100")
elif nota100 > 1:
    print(nota100, "Notas de R$ 100")
if nota50 == 1:
    print("1 Nota de R$ 50")
elif nota50 > 1:
    print(nota50, "Notas de R$ 50")
if nota10 == 1:
    print("1 Nota de R$ 10")
elif nota10 > 1:
    print(nota10, "Notas de R$ 10")
if nota5 == 1:
    print("1 Nota de R$ 5")
elif nota5 > 1:
    print(nota5, "Notas de R$ 5")
if nota1 == 1:
    print("1 Nota de R$ 1")
elif nota1 > 1:
    print(nota1, "Notas de R$ 1")