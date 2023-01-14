def primo(n):
    div = 2
    while n % div != 0 and div <= n / 2:
        div += 1
    if n % div == 0:
        return False
    else:
        return True

limite = int(input("Insira até onde deseja calcular os números primos: "))
n=2

while limite > n:
    if primo(n):
        print(n, end = " ")
    n += 1 