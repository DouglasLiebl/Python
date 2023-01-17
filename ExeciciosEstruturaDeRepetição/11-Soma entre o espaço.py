# Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = 0
if n1 > n2:
    for i in range(n1 + 1, n2):
        print(i, end = " ")
        soma = soma + i
elif n2 > n1:
    for i in range(n2 + 1, n1):
        print(i, end = " ")
        soma = soma + i 
else: 
    print("Os números são iguais")

print(soma) 