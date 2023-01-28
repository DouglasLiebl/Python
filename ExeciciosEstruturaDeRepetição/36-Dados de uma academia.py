# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

codigoCliente = 1
listaCodigos = []
listaPeso = []
listaAltura = []

while codigoCliente != 0:
    codigoCliente = int(input("Forneça o código de usuário: "))
    if codigoCliente == 0:
        break
    listaCodigos.append(codigoCliente)
    listaAltura.append(float(input("Insira sua altura: ")))
    listaPeso.append(float(input("Insira o seu peso: ")))

maiorAltura = listaAltura[0]
maiorPeso = listaPeso[0]
menorAltura = listaAltura[0]
menorPeso = listaPeso[0]
cont = 0
somaAlt = 0
somaP = 0
codeMeAlt = 0
codeMaAlt = 0
codeMeP = 0
codeMaP = 0

while cont < len(listaAltura) and cont < len(listaPeso):
    if listaAltura[cont] > maiorAltura:
        maiorAltura = listaAltura[cont]
        codeMaAlt = cont
    if listaAltura[cont] < menorAltura:
        menorAltura = listaAltura[cont]
        codeMeAlt = cont
    if listaPeso[cont] > maiorPeso:
        maiorPeso = listaPeso[cont]
        codeMaP = cont
    if listaPeso[cont] < menorPeso:
        menorPeso = listaPeso[cont]
        codeMeP = cont
    somaAlt += listaAltura[cont]
    somaP += listaPeso[cont]
    cont += 1

mediaAlt = somaAlt / len(listaAltura)
mediaP = somaP / len(listaPeso)

print(f"\n\nCliente mais Alto: {listaCodigos[codeMaAlt]}\n Altura: {maiorAltura} m\n Peso: {listaPeso[codeMaAlt]} kgs \nCliente mais Baixo: {listaCodigos[codeMeAlt]} \n Altura: {menorAltura} m\n Peso: {listaPeso[codeMeAlt]} kgs \nCliente com o maior Peso: {listaCodigos[codeMaP]}\n Peso: {maiorPeso} kgs\n Altura: {listaAltura[codeMaP]} m \nCliente com o menor Peso: {listaCodigos[codeMeP]}\n Peso: {menorPeso} kgs\n Altura: {listaAltura[codeMeP]} m \nMédia de Altura da academia: {mediaAlt:,.2f} m \nMédia de Peso da academia: {mediaP:,.2f} kgs")
