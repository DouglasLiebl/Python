# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

nPessoas = 0
idade = 0
soma = 0
print("Digite 'S' para parar de inserir idades")
while idade != 'S':
    idade = input("Insira sua idade: ")
    if idade == 'S':
        break
    nPessoas += 1
    soma = soma + int(idade)
media = soma / nPessoas
    
if media > 0 and media <= 25:
    print("O grupo de pessoas é considerado jovem")
elif media <= 26 and media >= 60:
    print("O grupo de pessoas é considerado adulto")
else:
    print("O grupo de pessoas é considerado idoso")     