# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

n = int(input("Digite um número que deseja calcular o fatorial: "))

cont = 1
n_fat = 1
while cont < n:
    cont += 1
    n_fat *= cont
    
print(f"O valor do fatorial de {n} é {n_fat}")