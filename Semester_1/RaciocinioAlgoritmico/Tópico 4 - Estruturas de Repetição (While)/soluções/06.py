# Escreva um programa que solicite um número inteiro e calcule a soma de seus dígitos.

numero_usuario = int(input("Digite um número inteiro: "))
soma_numeros = 0

while (numero_usuario > 0):
    digito = numero_usuario % 10
    soma_numeros += digito
    numero_usuario //= 10

print(f"Soma: {soma_numeros}")

