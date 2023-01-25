'''
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
'''
n = int(input("Insira o número do qual deseja calcular a tabuada: "))
nInicial = int(input("Insira o número inicial: "))
nFinal = int(input("Insira o número final: "))
if nFinal < nInicial:
    print("ERRO: O número final deve ser maior que o número inicial")
    nFinal = int(input("Insira o número final: "))

for i in range(nInicial, nFinal +1):
    resultado = n * i
    print(f"{n} X {i} = {resultado}")