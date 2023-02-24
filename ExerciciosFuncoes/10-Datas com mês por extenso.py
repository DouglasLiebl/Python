# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def data(x):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    dia = int(x[:2])
    mes = int(x[3:5])
    ano = int(x[6:])
    if int(dia) > 31 or (int(x[3:5]) - 1) > 12:
        return ("Data inválida")
    elif dia > 28 and mes == 2:
        return ("Data inválida")
    else:
        return (f"{dia} de {meses[mes - 1]} de {ano}")

x = input("Insira uma data [DD/MM/AAAA]: ")
print(data(x))