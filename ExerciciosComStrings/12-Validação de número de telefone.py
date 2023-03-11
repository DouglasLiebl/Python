'''
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
'''

def verificador():
    numero_telefone = input("Digite o número telefônico: ")
    if numero_telefone[4] == "-" and len(numero_telefone) == 9 or len(numero_telefone) == 8 and numero_telefone.find("-") == -1:
        print(f"Telefone válido! \nTelefone: {numero_telefone} \nTelefone com formatação: {numero_telefone[:4]}-{numero_telefone[4:]}")
    elif numero_telefone.find("-") != -1 and len(numero_telefone) == 8 or len(numero_telefone) == 7:
        numero = ["3"]
        for i in range(0,len(numero_telefone)):
            numero.append(numero_telefone[i])
        if "-" in numero:
            numero_telefone_s = ""
            numero_telefone_f = ""
            numero.remove("-")
            for i in range(0, 7):
                numero_telefone_s += numero[i]
            for i in range(0, 8):
                if i == 4:
                    numero_telefone_f += "-"
                    numero_telefone_f += numero[i]
                else:
                    numero_telefone_f += numero[i]
        
        print(f"Telefone: {numero_telefone} \nTelefone possui 7 dígitos. Vou acrescentar o digito três na frente... \nTelefone corrigido sem formatação: {numero_telefone_s} \nTelefone corrigido com formatação: {numero_telefone_f}")

verificador()