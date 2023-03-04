'''
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
'''

def escadaInv(nome):

    for i in range(0, len(nome)):
        print(nome[:(len(nome) - i)])

nome = input("Digite o seu nome de usuário: ")
escadaInv(nome)