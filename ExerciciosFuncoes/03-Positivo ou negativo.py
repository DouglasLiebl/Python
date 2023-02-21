#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def verificacao (x):
    if x <= 0:
        return "N"
    else:
        return "P"

n = int(input("Insira um número: "))
print(f"[P = positivo / N = negativo] \nO número digitado é {verificacao(n)}")