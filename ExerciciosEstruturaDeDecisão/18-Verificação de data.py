# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("Insira um dia: "))
mes = int(input("Insira um mês: "))
ano = int(input("Insira um ano: "))

validacao = False

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        validacao = True

if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        validacao = True

if mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0):
        if dia <= 29:
            validacao = True
    if (ano % 400 != 0):
        if dia <= 28:
            validacao = True

if validacao:
    print("Esta data é valida!")
else:
    print("Esta data é inválida")