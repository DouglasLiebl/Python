import math

print("Programa para calculo de equação de Bhaskara")

a = int(input("Forneça o valor de 'a': "))
b = int(input("Forneça o valor de 'b': "))
c = int(input("Forneça o valor de 'c': "))
deltar = 0

def delta (a):
    return int(math.pow(b, 2) + 4 * a * c)

def raiz (a):
    raiz1 = (-b + math.isqrt(delta(a))) / (2 * a)
    raiz2 = (-b - math.isqrt(delta(a))) / (2 * a)
    return raiz1, raiz2

if delta(a) < 0:
    print("Esta equação não possui raízes reais")
if delta(a) == 0:
    raiz(a)
    print("O valor da raíz é", raiz(a))
if delta(a) > 0:
    raiz(a)
    print("O valor das raízes são", raiz(a))