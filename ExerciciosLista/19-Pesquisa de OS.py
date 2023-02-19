'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''
def percentual(x, y):
    return (votosPorOs[y] / totalVotos) * 100

totalVotos = 0
oS = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votosPorOs = [0, 0, 0, 0, 0, 0]

n = 1

while n != 0:
    n = int(input("Qual o melhor Sistema Operacional para uso em servidores? \n1- Windows Server \n2- Unix \n3- Linux \n4- Netware \n5- Mac OS \n6- Outro \nAlternativa: "))
    while n > 6:
        n = int(input("ERRO: Opção inválida \nInsira a alternativa desejada novamente: "))
    if n == 0:
        break
    votosPorOs[n-1] += 1
    totalVotos += 1

cont = 0
maisVotado = votosPorOs[0]
print("\nSistema Operacional  Votos  Percentual \n-------------------  -----  ----------")
while cont < 6:
    print(f"{oS[cont]:<20} {votosPorOs[cont]:>5} {percentual(totalVotos, cont):>11,.1f} ")
    if votosPorOs[cont] > maisVotado:
        maisVotado = votosPorOs[cont]
        codeMaisV = cont
    cont += 1

print(f"-------------------  -----  ----------\nTotal {totalVotos:>20} {100:>10}% \nO Sistema Operacional mais votado foi o {oS[codeMaisV]}, com {votosPorOs[codeMaisV]} votos, correspondendo a {percentual(totalVotos, codeMaisV):,.1f}% dos votos.")

