''' 
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
  '''

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
media = (n1 + n2) / 2

if media <= 10.0 and media >= 9.0:
    conceito = 'A'

if media < 9.0 and media >= 7.5:
    conceito = 'B'

if media < 7.5 and media >= 6.0:
    conceito = 'C'

if media < 6.0 and media >= 4.0:
    conceito = 'D'

if media < 4.0 and media >= 0:
    conceito = 'E'

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    print(f"Dados do aluno: \n Nota da primeira prova: {n1:,.2f} \n Nota da segunda prova: {n2:,.2f} \n Média: {media:,.2f} \n Situação: APROVADO")
if conceito == 'D' or conceito ==  'E':
    print(f"Dados do aluno: \n Nota da primeira prova: {n1:,.2f} \n Nota da segunda prova: {n2:,.2f} \n Média: {media:,.2f} \n Situação: REPROVADO")