'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''

notas = []
soma = 0
media = 0
notasAbaixo7 = 0
notasAcimaMedia = 0
n = 0
continuar = 1

while continuar == 1:
    while n != -1:
        n = float(input("Insira o valor da nota: "))
        if n == -1:
            break
        else:
            notas.append(n)
            soma += n
    media = soma / len(notas)
    print(f"Foram lidas um total de {len(notas)} notas")

    cont = 0
    print(f"As notas lidas foram:", end = "")
    while cont < len(notas):
        print(f" {notas[cont]}", end = "")
        if notas[cont] < 7: 
            notasAbaixo7 += 1
        if notas[cont] > media: 
            notasAcimaMedia += 1
        cont += 1
        if cont == len(notas):
            print("\nNotas digitadas anteriormente, desta vez de forma invertida: ")
            cont -= 1
            while cont > -1:
                print(notas[cont])
                cont -= 1
            cont = (len(notas) + 1)
    print(f"Soma de todas as notas: {soma} \nMédia de todas as notas: {media} \nNotas acima da média: {notasAcimaMedia} \nNotas abaixo de 7: {notasAbaixo7}")
    continuar = input("Calculos finalizados! \nDeseja digitar um novo conjunto de notas? [S/N]: ")
    
    match continuar:
        case 'S':
            continuar = 1
            notas.clear
            n = 0
        case 'N':
            continuar = 0
    