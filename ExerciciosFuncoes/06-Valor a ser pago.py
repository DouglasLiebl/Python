'''
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''

def valorPagamento(prestacao, atraso):
    if atraso == 0:
        return prestacao
    elif atraso > 0:
        juros = ((atraso * 0.1) + 0.03) + 1
        prestacao = prestacao * juros
        return prestacao

stop = False
totalPagoDia = 0
nPagamentosDia = 0

print("[Insira prestação = 0 para encerrar o programa]")
while stop == False:
    prestacao = float(input("Insira o valor da prestação: "))
    if prestacao == 0:
        print(f"\nRelatório do dia: \nNúmero de prestações pagas: {nPagamentosDia} \nValor total dos pagamentos realizado: R$ {totalPagoDia:,.2f}")
        stop = True
        break
    atraso = int(input("Insira o número de dias em atraso: "))
    totalPagoDia += valorPagamento(prestacao, atraso)
    nPagamentosDia += 1
    print(f"Valor a ser pago: R$ {valorPagamento(prestacao, atraso):,.2f}")