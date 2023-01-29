'''
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
'''

n = int(input("Insira o termo final da série: "))
soma = 0
d1 = 0
d2 = 0
for i in range(0, n):
    if d1 == 0 and d2 == 0:
        d1 = 1
        d2 = 1
        print(f"S = {d1}/{d2}", end = " ")
    else:
        print(f"+ {d1}/{d2}", end = " ")
    soma += (d1/d2)
    d1 += 1
    d2 += 2
print(f"\nSoma da série: {soma:,.2f}")
