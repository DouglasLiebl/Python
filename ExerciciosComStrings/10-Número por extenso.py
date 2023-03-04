# Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

from num2words import num2words

def extenso(numero):
    numero = num2words(numero, lang = "pt-BR")
    return numero

numero = int(input("Insira um número: "))
print(extenso(numero).title())