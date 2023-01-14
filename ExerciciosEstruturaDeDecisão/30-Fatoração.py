n = int(input("Insira um número inteiro maior que 1: "))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        n = n / fator
        multiplicidade +=1
    if multiplicidade > 0:
        print("Fator:", fator, "Multiplicidade:", multiplicidade)
    fator += 1
    multiplicidade = 0