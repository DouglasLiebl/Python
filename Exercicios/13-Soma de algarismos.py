# Programa que soma os algarismos de um numero inserido pelo úsuario

numeroDig = int(input("Insira um numero sem limite de algarismos: "))

soma = 0
resto = 0
divisao = 1

while divisao != 0:
    divisao = numeroDig // 10
    resto = numeroDig % 10
    soma = soma + resto
    numeroDig = divisao

print("A soma dos algarismos do número digitado é", soma)    
