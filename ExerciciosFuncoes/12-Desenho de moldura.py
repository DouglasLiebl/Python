# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

def retangulo(l, c):

    for i in range(0, l):
        if i == 0 or i == (l - 1):
            for i in range(0, c):
                print(f"-", end = "")
        else:
            for i in range(0, c):
                if i == 0 or i == (c - 1):
                    print(f"|", end = "")
                else:
                    print(f"+", end = "")
        print("")
    return (f"Retângulo nas mediadas {l} x {c}")

l = int(input("Insira a largura do retângulo: "))
c = int(input("Insira o comprimento do retângulo: "))
print(retangulo(l,c))