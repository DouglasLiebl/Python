# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

numero = int(input("Digite um número: "))
numero = numero % 2

if numero == 0:
    print("O número digitado é par")
else:
    print("O número digitado é impar")