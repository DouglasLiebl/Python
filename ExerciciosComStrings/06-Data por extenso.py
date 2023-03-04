'''
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
'''

def dataExtenso(data):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    dia = data[:2]
    mes = data[3:5]
    ano = data[6:]
    print(f"Você nasceu em {dia} de {meses[int(mes) - 1]} de {ano}")

data = input("Insira a sua data de nascimento: ")
dataExtenso(data)