# Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

from random import randint

def randomizador(x):
    letras = []
    for i in range(0, len(x)):
        letras.append(x[i])
    x = ""
    for i in range(0, len(letras)):
        random = randint(0, len(letras) -1)
        x += letras[random]
        letras.pop(random)
    return x.lower()

x = input("Insira qualquer palavra: ")
print(randomizador(x))