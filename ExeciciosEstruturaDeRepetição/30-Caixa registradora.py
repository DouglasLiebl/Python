# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

print("Lojas Tabajara")
preco = 1
precoTotal = 0
i = 1
while preco != 0:
    preco = float(input(f"Produto {i}: R$ "))
    precoTotal = precoTotal + preco
    i += 1
    if preco == 0:
        print(f"Total: R$ {precoTotal:,.2f}")
        dinheiroCliente = float(input("Dinheito: R$ "))
        troco = dinheiroCliente - precoTotal
        print(f"Troco: R$ {troco:,.2f}")
        preco, i = 1, 1 
        print("Lojas Tabajara")   

