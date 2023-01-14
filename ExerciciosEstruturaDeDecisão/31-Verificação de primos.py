def primo(n):
    div = 2
    while n % div != 0 and div == n / 2:
        div += 1
    if n % div == 0:
        return False
    else:
        return True

n = int(input("Digite um número inteiro maior que 1: "))

while n > 0:
    if primo(n):
        print("É primo")
    else:
        print("Não é primo")
    n = int(input("Digite um número inteiro maior que 1: "))

if n == 0:
    exit()