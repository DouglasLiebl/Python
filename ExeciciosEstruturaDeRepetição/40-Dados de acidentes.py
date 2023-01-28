'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

cep = []
nVeiculos = []
nAcidentes = []

for i in range(0,5):
    cep.append(input("Insira o CEP da cidade: "))
    nVeiculos.append(int(input("Forneçao o número total de veículos: ")))
    nAcidentes.append(int(input("Forneça o número total de acidentes no ano: ")))

maiorIndice = 0
menorIndice = 100
cont = 0
nCep = 0
nCep2 = 0
nPc = 0
mediaV = 0
mediaA = 0

while cont < 5:
    percentual = (nAcidentes[cont] / nVeiculos[cont])
    if percentual > maiorIndice:
        maiorIndice = percentual
        nCep = cont
    if percentual < menorIndice:
        menorIndice = percentual
        nCep2 = cont
    if nVeiculos[cont] < 2000:
        mediaA = mediaA + nAcidentes[cont]
        nPc += 1
    mediaV += nVeiculos[cont]
    cont +=1
mediaV /= 5
mediaA /= nPc

print(f"Cidade com maior Indice de acidentes: {cep[nCep]} | Indice de {maiorIndice:,.2f}% \nCidade com o menor Indice de acidentes: {cep[nCep2]} | Indice de {menorIndice:,.2f}% \nNúmero médio de veiculos: {mediaV}")
if mediaA != 0:
    print(f"Número médio de acidentes em cidades com menos de 2000 veiculos: {mediaA}")