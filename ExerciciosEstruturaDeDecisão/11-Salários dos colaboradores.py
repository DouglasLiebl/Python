'''
 As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
 Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
-salários até R$ 280,00 (incluindo) : aumento de 20%
-salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-salários de R$ 1500,00 em diante : aumento de 5% 
 Após o aumento ser realizado, informe na tela:
-o salário antes do reajuste;
-o percentual de aumento aplicado;
-o valor do aumento;
-o novo salário, após o aumento.
'''

def aumento(n):
    return salario * n

salario = float(input("Insira o valor do salário: "))

if salario <= 280.00:
    aumento(1.20)
    valorAumento = aumento(1.20) - salario

    print(f"Dados do aumento: \n Salário antes do reajuste: R$ {salario} \n Percentual de aumento aplicado: 20% \n Valor do aumento: R$ {valorAumento:,.2f} \n Novo valor do salário após aumento: R$ {aumento(1.20):,.2f}")

if salario > 280.00 and salario < 700.00:
    aumento(1.15)
    valorAumento = aumento(1.15) - salario

    print(f"Dados do aumento: \n Salário antes do reajuste: R$ {salario} \n Percentual de aumento aplicado: 15% \n Valor do aumento: R$ {valorAumento:,.2f} \n Novo valor do salário após aumento: R$ {aumento(1.15):,.2f}")

if salario >= 700.00 and salario < 1500.00:
    aumento(1.10)
    valorAumento = aumento(1.10) - salario

    print(f"Dados do aumento: \n Salário antes do reajuste: R$ {salario} \n Percentual de aumento aplicado: 10% \n Valor do aumento: R$ {valorAumento:,.2f} \n Novo valor do salário após aumento: R$ {aumento(1.10):,.2f}")

if salario >= 1500.00:
    aumento(1.05)
    valorAumento = aumento(1.05) - salario

    print(f"Dados do aumento: \n Salário antes do reajuste: R$ {salario} \n Percentual de aumento aplicado: 5% \n Valor do aumento: R$ {valorAumento:,.2f} \n Novo valor do salário após aumento: R$ {aumento(1.05):,.2f}")
