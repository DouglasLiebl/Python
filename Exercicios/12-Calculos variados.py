'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a1-o produto do dobro do primeiro com metade do segundo .
a2-a soma do triplo do primeiro com o terceiro.
a3-o terceiro elevado ao cubo.

'''
import math

print("Você deve inserir dois números reais e um número inteiro logo abaixo:")

n1 = int(input("Insira o primeiro número inteiro: "))
n2 = int(input("Insira o segundo número inteiro: "))
n3 = float(input("Por fim, insira o número real: "))

a1 = (n1 * 2) * (n2 // 2)
a2 = (n1 * 3) + n3
a3 = math.pow(n3, 3)

print("O produto do dobro do primeiro com metade do segundo é",a1)
print("A soma do triplo do primeiro com o terceiro é", a2)
print("O número real elevado ao cubo é", a3)