# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

from random import randint

def embaralhador():
    continuar = True
    palavras = []

    with open('palavras.txt', 'r') as arquivo:
        for i in arquivo:
            palavras.append(i)

    while continuar:
        
        letras = []
        palavra_selecionada = palavras[randint(0,19)]
        palavra_embaralhada = ""
        erros = 0
            
        for i in range(0, len(palavra_selecionada)):
            letras.append(palavra_selecionada[i])
            if "\n" in letras:
                letras.pop(-1)
                palavra_selecionada = ""
                for i in range(0, len(letras)):
                    palavra_selecionada += letras[i]

        for i in range(0, len(letras)):
            random = randint(0, len(letras) - 1)
            palavra_embaralhada += letras[random]
            letras.pop(random)
        
        print(f"Você tem seis chances para acertar a palavra. \nA palavavra é {palavra_embaralhada.upper()}")
            
        while erros != 6:
            
            palavra_digitada = input("Digite qual a é palavra: ")
            
            if palavra_digitada.upper() == palavra_selecionada.upper():
                print(f"Você ganhou! A palavra era: {palavra_selecionada}")        
                break
            else: 
                erros += 1
                if erros == 6:
                    print(f"Você errou 6 vezes e perdeu. A palavra era: {palavra_selecionada}")
                    break
                else:
                    print(f"Você errou pela {erros}ª vez. Tente novamente.")

        verificar = input("Deseja jogar novamente? [S/N]: ")
        
        if verificar == "S" or verificar == "s":
            continuar = True
            continue
        else:
            continuar = False
            break

embaralhador()