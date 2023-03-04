'''
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
'''

def escada(nome):

    for i in range(0, len(nome)):
        print(nome[:(i + 1)])

nome = input("Digite o seu nome de usuário: ")
escada(nome)