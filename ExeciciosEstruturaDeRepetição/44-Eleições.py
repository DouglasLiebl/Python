'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''
voto = 1
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo = 0
branco = 0
while voto != 0:
    voto = int(input("[1] Cleiton \n[2] José \n[3] João \n[4] Cleber \n[5] Voto Nulo \n[6] Voto em Branco \nVoto: "))
    match voto:
        case 1:
            cand1 += 1
        case 2:
            cand2 += 1
        case 3:
            cand3 += 1
        case 4:
            cand4 += 1
        case 5:
            nulo += 1
        case 6:
            branco += 1

print(f"Resultados \n[1] Cleiton: {cand1} votos \n[2] José: {cand2} votos \n[3] João: {cand3} votos \n[4] Cleber: {cand4} votos \n[5] Voto Nulo: {nulo} votos \n[6] Voto em Branco: {branco} votos ")
