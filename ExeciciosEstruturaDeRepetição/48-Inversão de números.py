'''
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
'''

n = int(input("Insira um número inteiro positivo: "))
print("O número digitado fica, de forma invertida, assim: ")
while n % 10 != 0:
    resto = n % 10
    n //= 10
    print(resto, end = "")
