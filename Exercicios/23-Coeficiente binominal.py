n = int(input("Insira o valor de n: "))
k = int(input("Insira o valor de k: "))
p = n - k

def fatorial(n):
    if n:
        n_fat = 1
        cont = 1
        while cont < n:
            cont += 1
            n_fat *= cont
        
        return n_fat
    if k:
        k_fat = 1
        cont = 1
        while cont < k:
            cont += 1
            k_fat *= cont
        
        return k_fat

coeficiente = fatorial(n) / (fatorial(k) * fatorial(p))

print(f"O coeficiente binomial é {coeficiente:,.0f}")