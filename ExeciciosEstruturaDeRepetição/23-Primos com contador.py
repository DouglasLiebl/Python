# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

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

limitador = int(input("Digite até que número deseja calcular os primos: "))
n = 2
quantidadeDiv = 0
print(f"Números primos até {limitador}")
while limitador > n:
    if primo(n):
        print(n, end = " ")
    n += 1
    quantidadeDiv += 1

print(f"Foram realizadas {quantidadeDiv} divisões para encontrar os números acima")
