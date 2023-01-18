# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input("Qual termo da série de Fibonacci deseja encontrar: "))
stop = 1
ultimo, penultimo = 1, 0
while stop != n:
    novoTermo = ultimo + penultimo
    penultimo = ultimo
    ultimo = novoTermo
    stop += 1

print("O valor do termo desejado é ", ultimo)