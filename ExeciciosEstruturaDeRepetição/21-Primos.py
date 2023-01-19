# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

def primo(n):
    div = 2
    while n % div != 0:
        div += 1
        if n % div == 0:
            return False
        else:
            return True

n = int(input("Digite um número: "))
if primo(n):
    print("O número é primo")
else:
    print("O número não é primo")
