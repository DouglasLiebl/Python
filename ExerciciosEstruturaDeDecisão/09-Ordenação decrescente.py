# Faça um Programa que leia três números e mostre-os em ordem decrescente.

print("Insira três números:")
a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))
c = int(input("Insira o terceiro número: "))

if a < c:
    a, c = c, a
if b < c:
    b, c = c, b
if a < b:
    a, b = b, a

print(a, b, c)