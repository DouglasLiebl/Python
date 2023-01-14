def fatorial(n):
    cont = 1
    n_fat = 1
    while cont < n:
        cont += 1
        n_fat *= cont
    
    return n_fat

n = 1
while n > 0:
    n = int(input("Digite um número inteiro para calcular o fatorial: "))
    while n > 0:
        print(fatorial(n))
        n = 0
    continuar = input("Deseja digitar outro número? ")
    if continuar == 'sim':
        n = 1
    else: 
        n = 0
