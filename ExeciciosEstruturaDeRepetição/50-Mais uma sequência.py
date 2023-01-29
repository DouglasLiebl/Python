# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

n = int(input("Insira o termo final da série: "))
d1 = 1
for i in range(1, n):
    if d1 == 1:
        d1 = 2
        print(f"H = 1 + 1/{d1}", end = " ")
    else:
        print(f"+ 1/{d1}", end = " ")
    d1 += 1