# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(x, y):
    x = (x / 100) + 1
    custo = x * y   
    return custo

imposto = int(input("Insira a porcentagem de imposto: "))
custo = float(input("Insira o valor do produto: "))
print(f"O valor do produto acrescido com o imposto é: R${somaImposto(imposto, custo):,.2f}")