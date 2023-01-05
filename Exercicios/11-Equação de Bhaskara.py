import math

print("Programa para calculo de equação de Bhaskara")

a = int(input("Forneça o valor de 'a': "))
b = int(input("Forneça o valor de 'b': "))
c = int(input("Forneça o valor de 'c': "))

delta = (b **2) + (4 * a * c)

if delta < 0:
    print("Esta equação não possui raízes reais")
if delta == 0:
    raiz = (-b) / (2 * a)
    print("O valor da raíz é", raiz)
if delta > 0:
    raiz1 = (-b + math.isqrt(delta)) / (2 * a)
    raiz2 = (-b - math.isqrt(delta)) / (2 * a) 
    print("O valor das raízes são", raiz1, raiz2)