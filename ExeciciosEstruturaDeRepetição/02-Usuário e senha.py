# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

user = input("Insira o nome de usuário: ")
password = input("Insira a senha: ")

while password == user:
    print("ERRO: A senha não pode ser igual ao nome de usuário")
    user = input("Insira o nome de usuário: ")
    password = input("Insira a senha: ")
    
print("Informações salvas com sucesso")