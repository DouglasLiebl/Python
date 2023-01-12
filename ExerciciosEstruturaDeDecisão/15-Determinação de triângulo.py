'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
-Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
-Triângulo Equilátero: três lados iguais;
-Triângulo Isósceles: quaisquer dois lados iguais;
-Triângulo Escaleno: três lados diferentes;
'''
print("Digite as medidas dos três lados de um triângulo:")
l1 = float(input("Insira o lado um: "))
l2 = float(input("Insira o lado dois: "))
l3 = float(input("Insira o lado três: "))

if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
    print("Os dados fornecidos não podem formar um triângulo")

elif l1 == l2 == l3:
    print("Triângulo Equilátero")

elif l1 != l2 and l1 != l3 and l2 != l3:
    print("Triângulo Escaleno")

elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
    print("Triângulo Isósceles")

