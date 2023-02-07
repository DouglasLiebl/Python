'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
-salário bruto.
-quanto pagou ao INSS.
-quanto pagou ao sindicato.
-o salário líquido.
'''

horas = float(input("Insira quantas horas você trabalha por mês: "))
valorH = float(input("Agora insira quanto você ganha por hora trabalhada: "))

salarioB = valorH * horas
impostoR = salarioB - (salarioB * 0.89)
inss = salarioB - (salarioB * 0.92)
sindicato = salarioB - (salarioB  * 0.95)
salarioL = salarioB - (impostoR + inss + sindicato)

print(f"Valores dos descontos: \n -Salário Bruto: R${salarioB:,.2f} \n -INSS: {inss:,.2f} \n -Sindicato: R${sindicato:,.2f} \n -Imposto de Renda: R${impostoR:,.2f} \n -Salário Liquido: R${salarioL:,.2f}")
