n = int(input("Insira o valor de n: "))
k = int(input("Insira o valor de k: "))

def fatorial(n):
        n_fat = 1
        cont = 1
        while cont < n:
            cont += 1
            n_fat *= cont
        
        return n_fat

def coeficienteBinomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))

def testeFatorial():
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")

def testeCoeficiente():
    if coeficienteBinomial(5, 4) == 5:
        print("Funciona para n=5 e k=4")
    else:
        print("Não funciona para n=5 e k=4")
    if coeficienteBinomial(8, 6) == 15:
        print("Funciona para n=8 e k=6")
    else:
        print("Não funciona para n=8 e k=6")

print(f"O coeficiente binomial é {coeficienteBinomial(n, k):,.0f}")