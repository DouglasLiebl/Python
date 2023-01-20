# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

def fatorial(n):
    fat = 1
    print(f"{n}! =", end = " ")
    while n >= 1:
        fat = fat * n
        if n == 1:
            print(n, end = " = ")
            break
        print(n, end = ".")
        n -= 1
    return fat

n = int(input("Insira um número: "))
print(fatorial(n))