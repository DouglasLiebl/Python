'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
resposta = 0
respAfirmativas = []
perguntas = ['Telefonou para a vítima? ', 'Esteve no local do crime? ', 'Mora perto da vítima? ', 'Devia para a vítima? ', 'Já trabalhou com a vítima? ']

print("Responda com 'S' para sim e 'N' para não:")
for i in range(0, 5):
    resposta = (input(f"{perguntas[i]}"))
    if resposta == 'S':
        respAfirmativas.append(resposta)
    
if len(respAfirmativas) == 2:
    print("Suspeito!")
elif len(respAfirmativas) == 3 or len(respAfirmativas) == 4:
    print("Cúmplice!")
elif len(respAfirmativas) == 5: 
    print("Assassino!")
else:
    print("Inocente!")
