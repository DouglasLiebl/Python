# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. 

def soma(a, b, c):
    soma = a + b + c
    return soma

a = int(input("Insira o valor do primeiro número: "))
b = int(input("Insira o valor do segundo número: "))
c = int(input("Insira o valor do terceiro número: "))

print(f"A soma dos números digitados anteriormente é {soma(a, b, c)}")