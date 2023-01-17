# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

anos = 0
n = True
print("Quantos anos levará para que a população da cidade A ultrapasse a cidade B: \n")

while n:
    cidadeA = float(input("Insira a população da cidade A: "))
    while cidadeA != round(cidadeA):
        print("ERRO: Insira um número inteiro")
        cidadeA = float(input("Insira a população da cidade A: "))
    taxaA = float(input("Insira a taxa de crescimento, em %, da cidade A: "))
    while taxaA <= 0:
        print("ERRO: Insira uma taxa de crescimento válida")
        taxaA = float(input("Insira a taxa de crescimento, em %, da cidade A: "))
    
    cidadeB = float(input("Insira a população da cidade B: "))
    while cidadeB != round(cidadeB):
        print("ERRO: Insira um número inteiro")
        cidadeB = float(input("Insira a população da cidade B: "))
    taxaB = float(input("Insira a taxa de crescimento, em %, da cidade B: "))
    while taxaB <= 0:
        print("ERRO: Insira uma taxa de crescimento válida")
        taxaB = float(input("Insira a taxa de crescimento, em %, da cidade B: "))
    while cidadeA <= cidadeB:
        cidadeA = cidadeA * (1 + (taxaA / 100))
        cidadeB = cidadeB * (1 + (taxaB / 100))
        anos += 1
    print("A cidade A ultrapassará ou iguala a população da cidade B em %d anos" %anos)
    repeat = input("Deseja realizar o cálculo novamente com outros valores? [S/N] ")
    match repeat:
        case 'S':
            n = True
            anos == 0
        case 'N':
            n = False