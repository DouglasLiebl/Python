# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horas = input("Insira quantas horas você trabalha por mês: ")
valorH = input("Agora insira quanto você ganha por hora trabalhada: ")

horas = int(horas)
valorH = int(valorH)

salario = horas * valorH

print("O salário no mês refetido é", salario, "reais")
