# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

def primo (n):
    div = 2
    while n % div != 0 and div <= n / 2:
        div += 1
        if n == 2:
            return True
        elif n % div == 0:
            return False
        else:
            return True

n = int(input("Insira um número inteiro: "))
if primo(n):
    print("O número fornecido é primo")
else:
    print("O número fornecido não é primo")
    