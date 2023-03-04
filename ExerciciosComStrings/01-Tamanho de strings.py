'''
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''

def strings (string1, string2):

    if len(string1) == len(string2) and string1 == string2:
        return print(f"{string1} \n{string2} \nAs duas strings são de mesmo tamanho. \nAs duas strings possuem o mesmo conteúdo.")
    else: 
        return print(f"{string1} \n{string2} \nAs duas strings são de tamanhos diferentes \nAs duas strings possuem conteúdo diferente.")
    

string1 = input("Insira a primeira frase: ")
string2 = input("Insira a segunda frase: ")

strings(string1, string2)