'''
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
'''
def conversor(x):
    MB = x / (1024 **2)
    return MB

def percentual(x, y):
    percentual = (y / x) * 100
    return percentual

espaco = []
usuario = []


with open('usuarios.txt','r') as arquivo:
    for i in arquivo:
        usuario.append(i[:15])
        espaco.append(int(i[15:]))
    with open('relatório.txt', 'w') as arquivo:
        arquivo.write(str("ACME Inc.               Uso do espaço em disco pelos usuário \n------------------------------------------------------------------------ \nNr.  Usuário        Espaço utilizado     %do uso\n"))
        espacoTotal = conversor(sum(espaco))
        espacoMedio = espacoTotal / len(usuario)
        
        for i in range(0, len(usuario)):
            arquivo.write(str(f"{i + 1:<4} {usuario[i].strip():<10} {conversor(espaco[i]):>11,.2f} MB {percentual(espacoTotal, conversor(espaco[i])):>16,.2f}%\n"))
        arquivo.write(str(f"\nEspaço total ocupado: {espacoTotal:,.2f} MB \nEspaço médio ocupado: {espacoMedio:,.2f} MB"))
        
