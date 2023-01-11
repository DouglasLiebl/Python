'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
---Desconto do IR:
-Salário Bruto até 900 (inclusive) - isento
-Salário Bruto até 1500 (inclusive) - desconto de 5%
-Salário Bruto até 2500 (inclusive) - desconto de 10%
-Salário Bruto acima de 2500 - desconto de 20%
'''
def fgts(n):
    return salario - (salario * n)

def impostoRenda(n):
    return salario - (salario * n)

def sindicato(n):
    return salario - (salario * n)

valorHora = float(input("Insira o valor da sua hora: "))
horasTrab = float(input("Insira a quantidade de horas trabalhadas no mês: "))
salario = valorHora * horasTrab

if salario <= 900.00:
    fgts(0.89)
    sindicato(0.97)
    salarioLiquido = salario - sindicato(0.97)
    totalDescontos = sindicato(0.97)
    print(f"Salário Bruto: ({valorHora} * {horasTrab}): R$ {salario:,.2f} \n(-) IR: Isento \n(-) Sindicato (3%): R$ {sindicato(0.97):,.2f} \nFGTS (11%): R$ {fgts(0.89):,.2f} \nTotal de descontos: R$ {totalDescontos:,.2f} \nSalário líquido: R$ {salarioLiquido:,.2f}") 

if salario > 900.00 and salario <= 1500.00:
    fgts(0.89)
    sindicato(0.97)
    impostoRenda(0.95)
    salarioLiquido = salario - sindicato(0.97) - impostoRenda(0.95)
    totalDescontos = sindicato(0.97) + impostoRenda(0.95)
    print(f"Salário Bruto: ({valorHora} * {horasTrab}): R$ {salario:,.2f} \n(-) IR (5%): R$ {impostoRenda(0.95):,.2f} \n(-) Sindicato (3%): R$ {sindicato(0.97):,.2f} \nFGTS (11%): R$ {fgts(0.89):,.2f} \nTotal de descontos: R$ {totalDescontos:,.2f} \nSalário líquido: R$ {salarioLiquido:,.2f}") 

if salario > 1500.00 and salario <= 2500.00:
    fgts(0.89)
    sindicato(0.97)
    impostoRenda(0.90)
    salarioLiquido = salario - sindicato(0.97) - impostoRenda(0.90)
    totalDescontos = sindicato(0.97) + impostoRenda(0.90)
    print(f"Salário Bruto: ({valorHora} * {horasTrab}): R$ {salario:,.2f} \n(-) IR (10%): R$ {impostoRenda(0.80):,.2f} \n(-) Sindicato (3%): R$ {sindicato(0.97):,.2f} \nFGTS (11%): R$ {fgts(0.90):,.2f} \nTotal de descontos: R$ {totalDescontos:,.2f} \nSalário líquido: R$ {salarioLiquido:,.2f}") 

if salario > 2500.00:
    fgts(0.89)
    sindicato(0.97)
    impostoRenda(0.80)
    salarioLiquido = salario - sindicato(0.97) - impostoRenda(0.80)
    totalDescontos = sindicato(0.97) + impostoRenda(0.80)
    print(f"Salário Bruto: ({valorHora} * {horasTrab}): R$ {salario:,.2f} \n(-) IR (20%): R$ {impostoRenda(0.80):,.2f} \n(-) Sindicato (3%): R$ {sindicato(0.97):,.2f} \nFGTS (11%): R$ {fgts(0.89):,.2f} \nTotal de descontos: R$ {totalDescontos:,.2f} \nSalário líquido: R$ {salarioLiquido:,.2f}") 


