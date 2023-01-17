#S upondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

cidadeA = 80000
cidadeB = 200000
anos = 0

while cidadeA <= cidadeB:
    cidadeA = cidadeA * 1.03
    cidadeB = cidadeB * 1.015
    anos += 1 

print("A cidade A ultrapassará ou iguala a população da cidade B em %d anos" %anos)