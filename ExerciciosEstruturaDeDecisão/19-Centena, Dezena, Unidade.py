# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

numero = int(input("Insira um número inteiro menor que 1000: "))
if numero > 1000:
    exit()

centena, dezena, unidade = 0, 0, 0

if numero >= 100:
    centena = numero // 100
    dezena = numero % 100
    numero = dezena

if numero < 100 :
    dezena = numero // 10
    unidade = numero % 10
    
if numero < 10:
    unidade = numero

if centena > 0 and dezena > 0 and unidade > 0:
    print(f"O número digitado possui {centena} centenas, {dezena} dezenas e {unidade} unidades")
elif centena > 0 and dezena > 0 and unidade <= 0:
    print(f"O número digitado possui {centena} centenas e {dezena} dezenas")
elif centena > 0 and dezena <= 0 and unidade > 0:
    print(f"O número digitado possui {centena} centenas e {unidade} unidades")
elif centena <= 0 and dezena > 0 and unidade > 0:
    print(f"O número digitado possui {dezena} dezenas e {unidade} unidades")
elif centena <= 0 and dezena > 0 and unidade <= 0:
    print(f"O número digitado possui {dezena} dezenas")
elif centena <= 0 and dezena <= 0 and unidade > 0:
    print(f"O número digitado possui {unidade} unidades")
else:
    print("Esse número não possui centenas, dezenas e nem unidades")