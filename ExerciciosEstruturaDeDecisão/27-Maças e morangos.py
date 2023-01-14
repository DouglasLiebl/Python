'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

'''
macas = float(input("Quantos quilos de maça deseja? "))
morango = float(input("Quantos quilos de morango deseja? "))

if macas > 5.00:
    precoMa = macas * 1.50
else:
    precoMa = macas * 1.80

if morango > 5.00:
    precoMo = morango * 2.20
else: 
    precoMo = morango * 2.50

pesoTotal = macas + morango
precoTotal = precoMa + precoMo

if pesoTotal > 8.00 or precoTotal > 25.00:
    precoTotal = precoTotal * 0.90

print(f"O valor total é de R$ {precoTotal:,.2f}")
