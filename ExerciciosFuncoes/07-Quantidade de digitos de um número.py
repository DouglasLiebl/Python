# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def digitos(n):
    return len(n)

n = input("Insira um número inteiro: ")
if digitos(n) > 1:
    print(f"O número digitado possui {digitos(n)} dígitos")
else:
    print("O número digitado possui apenas um dígito")