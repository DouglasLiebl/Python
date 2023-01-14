'''
Faça um programa que leia e valide as seguintes informações:
-Nome: maior que 3 caracteres;
-Idade: entre 0 e 150;
-Salário: maior que zero;
-Sexo: 'f' ou 'm';
-Estado Civil: 's', 'c', 'v', 'd';
'''
nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
sexo = input("Insira o seu sexo: [F/M] ")
estCiv = input("Insira seu estado civil: [S/C/V/D] ")
n = 1
while n == 1 :
    while len(nome) < 3:
        print("ERRO: Insira um nome válido") 
        nome = input("Insira seu nome: ")
    while idade < 0 or idade > 150:
        print("ERRO: Insira uma idade válida")
        idade = int(input("Insira sua idade: "))
    while sexo != 'F' and sexo != 'M':
        print("ERRO: Insira um sexo válido")
        sexo = input("Insira o seu sexo: [F/M] ")
    while estCiv != 'S' and estCiv != 'C' and estCiv != 'V' and estCiv != 'D':
        print("ERRO: Insira um estado civil válido")
        estCiv = input("Insira seu estado civil: [S/C/V/D] ")
    n = 0

print("Informações válidadas com sucesso!")