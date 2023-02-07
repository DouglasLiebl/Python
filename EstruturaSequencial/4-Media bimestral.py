# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

aluno = input("Nome do aluno: ")
n1 = input("Nota do primeiro bimestre: ")
n2 = input("Nota do segundo bimestre: ")
n3 = input("Nota do terceiro bimestre: ")
n4 = input("Nota do quarto bimestre: ")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)

media = (n1 + n2 + n3 + n4)/4

print("A media do aluno", aluno, "é", media)