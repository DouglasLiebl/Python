'''
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

codigo = 'S'
pedidos = []
valores = []
quantidades = []
print("Pressione 'E' para encerrar o pedido")
while codigo != 'N':
    codigo = input("Insira o código do produto: ")
    total = 0
    match codigo:
        case '100':
            quant = int(input("Insira a quantidade: "))
            quantidades.append(quant)
            valores.append(quant * 1.20)
            pedidos.append('Cachorro Quente')
        case '101':
            quant = int(input("Insira a quantidade: "))
            quantidades.append(quant)
            valores.append(quant * 1.30)
            pedidos.append('Bauru Simples')
        case '102':
            quant = int(input("Insira a quantidade: "))
            quantidades.append(quant)
            valores.append(quant * 1.50)
            pedidos.append('Bauru com ovo')
        case '103':
            quant = int(input("Insira a quantidade: "))
            quantidades.append(quant)
            valores.append(quant * 1.20)
            pedidos.append("Hambúrguer")
        case '104':
            quant = int(input("Insira a quantidade: "))
            quantidades.append(quant)
            valores.append(quant * 1.30)
            pedidos.append('Chesseburguer')
        case '105':
            quant = int(input("Insira a quantidade: "))
            quantidades.append(quant)
            valores.append(quant * 1.00)
            pedidos.append('Refrigerante')
        case 'E':
            stop = 0
            print("Produto        Quantidade  Preço")
            while stop < len(valores):
                total += valores[stop]
                print(f"{pedidos[stop]:<14} {quantidades[stop]:<11} R$ {valores[stop]:,.2f} ")
                stop += 1
            print(f"\nValor total {'R$':>17} {total:,.2f}")
            codigo = input("Deseja inserir uma novo pedido? [S/N] ")
            pedidos = []
            valores = []
            quantidades = []
        case _:
            print("ERRO: código digitado inválido, tente novamente")
        