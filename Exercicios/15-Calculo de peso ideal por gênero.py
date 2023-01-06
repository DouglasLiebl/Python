'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
'''

genero = input("Para que seu peso ideal seja calculado selecione uma alternativa: \n [1] Masculino \n [2] Feminino \n Alternativa: ")

match genero:
    case '1':
        altura = float(input("Agora insira sua altura: "))
        pesoIdeal = (72.7 * altura) - 58
        print(f"O seu peso ideal é {pesoIdeal:,.2f} quilos")
    case '2':
        altura = float(input("Agora insira sua altura: "))
        pesoIdeal = (62.1 * altura) - 44.7
        print(f"O seu peso ideal é {pesoIdeal:,.2f} quilos")

