# Escreva um programa que peça um número inteiro e exiba a sua tabuada de multiplicação de 1 a 10.

numero_usuario = int(input("Digite um número inteiro: "))

print(f"Aqui está a tabuada de {numero_usuario} de 1 a 10:")

i = 1

while(i <= 10):
    print(f"{numero_usuario} x {i} = {i * numero_usuario}")
    i += 1
