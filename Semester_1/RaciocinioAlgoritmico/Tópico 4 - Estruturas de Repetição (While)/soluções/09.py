# Escreva um programa que exiba uma tabela de conversão de graus Celsius para Fahrenheit, de -10 até 100 celsius.

temperatura_f = 0

temperatura_c = -10
while(temperatura_c <= 100):
    temperatura_f = (temperatura_c * 1.8) + 32
    print(f"{temperatura_c}ºC é {temperatura_f:.2f}ºF")
    temperatura_c += 1

