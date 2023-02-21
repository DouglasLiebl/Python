# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def conversor(h, m):
    h = int(h)
    if h < 12:
        return (f"0{h}:{m} A.M.")
    else:
        h -= 12
        return (f"0{h}:{m} P.M.")

stop = "S"
print("[Usar '0' para horas abaixo de 12. EX: 08:50]")
while stop == "S" or stop == "s":
    horario = input("Insira o horário a ser convertido: ")
    print(f"{conversor(horario[:2], horario[3:])}")
    stop = input("Deseja continuar convertendo? [S/N] ")
    if stop == "S" or stop == "s":
        continue
    else:
        break