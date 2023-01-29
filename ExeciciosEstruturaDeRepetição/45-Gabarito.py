'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
'''
respostas = []
gabarito = ['A','B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
notas = []
nota = 0
totalAlunos = 0
continuar = 'S'
alternativa = 0
N = True
while N:
    for i in range(1, 11):
        respostas.append(input(f"Digite a resposta da questão {i}: "))
        if respostas[alternativa] == gabarito[alternativa]:
            nota += 1
        alternativa += 1
    print(f"A sua nota foi: {nota}")
    notas.append(nota)
    totalAlunos += 1
    nota = 0
    alternativa = 0
    respostas = []
    continuar = input("Outro aluno deseja verificar sua nota? [S/N] ")
    if continuar == 'N':
        maiorNota = 0
        menorNota = 11
        stop = 0
        media = 0
        while stop < len(notas):
            if maiorNota < notas[stop]:
                maiorNota = notas[stop]
            if menorNota > notas[stop]:
                menorNota = notas[stop]
            media += notas[stop]
            stop += 1 
        N = False

media /= totalAlunos
print(f"O programa verificou as notas de {totalAlunos} alunos \nA maior nota foi {maiorNota} e a menor foi {menorNota} \nA média das notas digitadas foi: {media:,.1f}")