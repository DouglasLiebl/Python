igual = True

numero = int(input("Digite um número com pelo menos dois algarismos: "))

divisao = 1
digito1 = 1
digito2 = 0
divisao2 = 1


while divisao2 != 0 and igual:
    divisao = numero // 10
    digito1 = numero % 10
    numero = divisao
    divisao2 = divisao // 10
    digito2 = divisao % 10
    if digito1 == digito2:
        igual = False

if igual:
    print("Não existem algarismos adjacentes no número digitado")
else:
    print("Existem algarismos adjacentes no número digitado!")
