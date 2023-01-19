# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

def primo(n):
    div = 2
    while n % div != 0:
        div += 1
        if n % div == 0:
            return False
        else:
            return True

def divisores(n):
    div = 1
    divisores = []
    while n >= div:
        if n % div == 0:
            divisores.append(div)
        div += 1
    return divisores


n = int(input("Insira um número: "))
if primo(n):
    print("O número digitado é primo")
else: 
    print(f"O número digitado não é primo e seus divisores são", divisores(n))