'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''

salarioInicial = float(input("Insira o valor do salário: "))
anoInicial = int(input("Insira o ano da contratação: "))
anoFinal = int(input("Insira até qual ano deseja calcular o salário: "))
aumento = 0.015

for i in range(anoInicial +1, anoFinal + 1):
    salarioFinal = (salarioInicial * (1 + aumento))
    salarioInicial = salarioFinal
    aumento *= 2
    print(f"O salário em {i} é de R$ {salarioFinal:,.2f}")