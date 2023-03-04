'''
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
'''

def contador(frase):
    vogais = ["a", "e", "i", "o", "u"]
    vogaisT = 0
    espacos = frase.count(" ")

    for i in range(0, 5):
        vogaisT += frase.count(vogais[i])
    
    return (f"Números de espaços em branco na frase: {espacos} \nNúmeros total de vogais na frase: {vogaisT}")

frase = input("Insira uma frase ou palavra: ")
print(contador(frase))