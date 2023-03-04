'''
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

F
U
L
A
N
O
'''

def nomeVertical(nome):
    
    for i in range(0, len(nome)):
        print(nome[i])
    
nome  = input("Digite o seu nome de usuário: ")    
nomeVertical(nome)