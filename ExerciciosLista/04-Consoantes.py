# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
caracteres = []
vogais = []
for i in range(0, 10):
    caracteres.append(input(f"Forneça a {i + 1}ª letra: "))
    if caracteres [i] == 'a' or caracteres [i] == 'e' or caracteres [i] == 'i' or caracteres [i] == 'o' or caracteres [i] == 'u':
        vogais.append(caracteres[i])

for i in range(0, len(vogais)):
    caracteres.remove(vogais[i]) 

print(f"Foram digitas {len(caracteres)} consoantes, sendo elas {caracteres}")