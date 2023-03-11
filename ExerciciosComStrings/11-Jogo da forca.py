'''
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
'''

from random import randint

def forca():
    palavras = []
    continuar = True

    with open('palavras.txt', 'r') as arquivo:
        for i in arquivo:
            palavras.append(i)
        
    while continuar:
        erros = 0
        palavra_selecionada = palavras[randint(0, 19)]
        palavra_selecionada = palavra_selecionada.upper()
        letras = []
        letras_corretas = []

        for i in range(0, (len(palavra_selecionada))):
            letras.append(palavra_selecionada[i])
            letras_corretas.append("_")
            if "\n" in letras:
                palavra_selecionada = ""
                letras.pop(-1)
                for i in range(0, len(letras)):
                    palavra_selecionada += letras[i]
        print("_ " * len(palavra_selecionada))
        
        while erros != 6:
            acertos = ""
            letra = input("Digite uma letra: ")
            
            if palavra_selecionada.find(letra.upper()) != -1: 
                if letra in letras_corretas:
                    letra = input("Letra já digitada \nDigite uma letra novamente: ")
                for i in range(0, (len(palavra_selecionada))):
                    if letras[i] == letra.upper():
                        letras_corretas[i] = letra
                for i in range(0, (len(palavra_selecionada))):
                    print(letras_corretas[i].upper(), end = " ")
                    acertos += letras_corretas[i]
                print("")

            elif palavra_selecionada.find(letra.upper()) == -1:
                erros += 1
                if erros == 6:
                    print(f"Você perdeu! A palavra era {palavra_selecionada}")
                    break
                else:    
                    print(f"Você errou pela {erros}ª vez. Tente de novo!")

            if acertos.upper() == palavra_selecionada:
                print(f"Você ganhou! A palavra era {palavra_selecionada}")
                break
         
        verificar = input("Deseja continuar jogando? [S/N]: ")
        if verificar == "S" or verificar == "s":
            continue
        else:
            continuar = False
            

forca()