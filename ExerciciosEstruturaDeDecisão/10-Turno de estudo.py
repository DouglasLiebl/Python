# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Em qual turno você estuda? \n [M] Matutino \n [V] Vespertino \n [N] Noturno \n Turno: ")

match turno:
    case 'M':
        print("Bom Dia!")
    case 'V':
        print("Boa Tarde!")
    case 'N':
        print("Boa Noite!")
    case other:
        print("Valor Inválido")
