# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

from random import randint
def craps ():
    resultado = 0
    for i in range(0,2):
        random = randint(1, 6)
        resultado += random
    
    if resultado == 7 or resultado == 11:
        return "Você ganhou!"
    elif resultado == 2 or resultado == 3 or resultado == 12:
        return "Você perdeu! Tente novamente"
    elif resultado in range(4, 7) or resultado in range(8, 11):
        print(f"Você tirou o número {resultado}, pressione \"S\" para rolar os dados novamente até que ele saia novamente, porém você perde se 7 sair antes: ")
        s = input()
        ponto = resultado
        while s == "S":
            random = randint(1, 12)
            if random == ponto:
                return ("Você ganhou!")
            elif random == 7:
                return ("Você perdeu! Mais sorte na próxima")
            else:
                print(f"Resultado: {random}")
        
print(craps())