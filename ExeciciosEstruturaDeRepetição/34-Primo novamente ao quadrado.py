# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

def primo(n):
    div = 2
    if n == 2:
            return True
    while n % div != 0 and div <= n / 2:
        div += 1
    if n % div == 0:
        return False
    else:
        return True

limite = int(input("Insira até onde deseja encontrar primos: "))
n = 2

while n != limite:
    if primo(n):
        print(n, end = " ")
    n += 1

