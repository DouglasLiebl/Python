# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

print("Digite dez números:")
par = 0
impar = 0
for i  in range(0,10):
    i = int(input("Digite um número: "))
    if i % 2 == 0:
        par += 1
    else:
        impar += 1

if par > 0 and impar == 0:
    print("Todos os 10 números digitados são pares")
elif impar > 0 and par == 0:
    print("Todos os dez números digitados são impares")
else:
    print(f"Dos números digitados, {par} são pares e {impar} são impares")