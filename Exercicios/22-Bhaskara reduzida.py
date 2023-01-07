import math

print("Programa para calculo de equação de Bhaskara")

a = int(input("Forneça o valor de 'a': "))
b = int(input("Forneça o valor de 'b': "))
c = int(input("Forneça o valor de 'c': "))

def delta ():
    global a, b, c
    return int(math.pow(b, 2) + 4 * a * c)

def raiz ():
    global a, b, c
    raiz1 = (-b + math.isqrt(delta())) / (2 * a)
    raiz2 = (-b - math.isqrt(delta())) / (2 * a)
    return raiz1, raiz2

if delta() < 0:
    print("Esta equação não possui raízes reais")
if delta() == 0:
    raiz()
    print("O valor da raíz é", raiz())
if delta() > 0:
    raiz()
    print("O valor das raízes são", raiz())