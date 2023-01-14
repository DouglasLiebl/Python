'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
-"Telefonou para a vítima?"
-"Esteve no local do crime?"
-"Mora perto da vítima?"
-"Devia para a vítima?"
-"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
print("Responda apenas com Sim ou Não:")
p1 = input("Telefonou para a vítima? ")
p2 = input("Esteve no local do crime? ")
p3 = input("Mora perto da vítima? ")
p4 = input("Devia para a vítima? ")
p5 = input("Já trabalhout com a vítima? ")
classificacao = 0

if p1 == 'sim':
    classificacao += 1
if p2 == 'sim':
    classificacao += 1
if p3 == 'sim':
    classificacao += 1
if p4 == 'sim':
    classificacao += 1
if p5 == 'sim':
    classificacao += 1

if classificacao == 2:
    print("Suspeita")
elif classificacao == 3 or classificacao == 4:
    print("Cúmplice")
elif classificacao == 5:
    print("Assassino")
else:
    print("Inocente") 
