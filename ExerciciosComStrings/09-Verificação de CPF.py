# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

def verificador(cpf):
    if cpf[3] == "." and cpf[7] == "." and cpf[11] == "-":
        return ("CPF válido")
    else:
        return ("CPF inválido")
    
CPF = input("Insira o seu CPF: ")
print(verificador(CPF))