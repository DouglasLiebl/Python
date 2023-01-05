# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

Fahrenheit = input("Insira a temperatura em Fahrenheit: ")

Fahrenheit = float(Fahrenheit)
Celsius = 5 * ((Fahrenheit - 32) / 9)

print("A valor equivalente, em Celcius, é", Celsius, "graus")