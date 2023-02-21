# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(n):
    reverso = str()
    for i in range(0, len(str(n))):
        divisao = n // 10
        resto = n % 10
        reverso += str(resto)
        n = divisao
    return reverso

n = int(input("Insira um número inteiro com mais de uma casa decimal: "))
print(f"O reverso do número digitado é {reverso(n)}")