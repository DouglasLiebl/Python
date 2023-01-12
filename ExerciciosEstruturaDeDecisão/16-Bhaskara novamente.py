'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
-Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
-Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
-Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
-Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
import math

print("Programa para calculo de equação de Bhaskara")

a = int(input("Forneça o valor de 'a': "))

if a == 0:
    print("A equação não é do segundo grau. O programa não pode continuar")
    exit()

b = int(input("Forneça o valor de 'b': "))
c = int(input("Forneça o valor de 'c': "))


def delta (a):
    return int(math.pow(b, 2) + 4 * a * c)

def raiz (a):
    raiz1 = (-b + math.isqrt(delta(a))) / (2 * a)
    raiz2 = (-b - math.isqrt(delta(a))) / (2 * a)
    if delta(a) == 0:
        return raiz1
    if delta(a) > 0:
        return raiz1, raiz2
    

if delta(a) < 0:
    print("Esta equação não possui raízes reais")
if delta(a) == 0:
    raiz(a)
    print("O valor da raíz é", raiz(a))
if delta(a) > 0:
    raiz(a)
    print("O valor das raízes são", raiz(a))