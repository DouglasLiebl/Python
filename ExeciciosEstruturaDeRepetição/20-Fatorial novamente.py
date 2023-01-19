# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

f = True
while f:
    n = int(input("Digite um número para que seu fatorial seja calculado: "))
    while n < 0 or n > 15:
        print("ERRO: Apenas números maiores que 0 e menores que 16 são aceitos")
        n = int(input("Digite um número para que seu fatorial seja calculado: "))
    cont = 1
    n_fat = 1
    while cont < n:
        cont += 1
        n_fat *= cont
    print(f"O fatorial do número é {n_fat}")
    f = input("Deseja calcular mais? [S/N] ")
    if f == 'S':
        f = True
    else:
        f = False