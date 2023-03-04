# a função "sqrt" fornece a raiz perfeita de um número, ou seja, retorna o valor com ponto flutuante caso seja necessario
from math import sqrt
n = int(input("Insira um número: "))
dobro = n * 2
triplo = n * 3
raiz = float(sqrt(n))
print(f"O dobro de {n} vale {dobro}, o triplo vale {triplo} e sua raiz quadrada é {raiz:,.2f}")

# Já a função "isqrt" retorna a raiz de forma arredondada, ou seja, o número mais proximo da raiz, por exemplo, a raiz de 5 seria 2.24, essa função retornaria 2.00

from math import isqrt
n = int(input("Insira um número: "))
dobro = n * 2
triplo = n * 3
raiz = float(isqrt(n))
print(f"O dobro de {n} vale {dobro}, o triplo vale {triplo} e sua raiz quadrada é {raiz}")
