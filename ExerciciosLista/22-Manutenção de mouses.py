'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''
def percentual(x, y):
    return (quantidade[y] / totalMouses) * 100
tipoDefeito = ["Necessita da esfera", "Necessita de limpeza", "Necessita troca do cabo ou do conector", "Quebrado ou inutilizado"]
quantidade = [0, 0, 0, 0]
totalMouses = 0
continuar = True
while continuar:
    identificacao = int(input("Insira a identificação do mouse: "))
    if identificacao == 0:
        continuar = False
        print(f"Quantidade de mouses: {totalMouses}\n\nSituação                            Quantidade         Percentual")
        stop = 0
        while stop < 4:
            print(f"{stop + 1}- {tipoDefeito[stop]:<40} {quantidade[stop]:< 13} {percentual(totalMouses, stop):,.2f}%")
            stop += 1
        break
    codDefeito = int(input("Insira o código do defeito: "))
    while codDefeito > 4 or codDefeito == 0:
        codDefeito = int(input("ERRO: Código inválido \nInsira o código do defeito: "))
    quantidade[codDefeito - 1] += 1
    totalMouses += 1