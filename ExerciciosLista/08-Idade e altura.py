# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []

for i in range(0, 5):
    idade.append(int(input("Insira a sua idade: ")))
    altura.append(float(input("Agora insira sua altura: ")))

cont = 0
stop = True
while stop:
    print("Ordem de inserção: ")
    while cont < 5:
        print(f"Idade: {idade[cont]}   Altura: {altura[cont]:,.2f}")
        cont += 1
    print("Ordem inversa: ")
    cont = 4
    while cont >= 0 :
        print(f"Idade: {idade[cont]}   Altura: {altura[cont]:,.2f}")
        cont -= 1
    stop = False
