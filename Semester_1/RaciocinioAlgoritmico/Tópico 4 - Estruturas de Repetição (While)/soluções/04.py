# Escreva um programa que gere um número aleatório entre 1 e 100 e peça para o usuário adivinhá-lo.

import random

numero_aleatorio = random.randint(1, 100)

numero_escolhido = int(input("Digite um número entre 1 e 100: "))

if numero_escolhido == numero_aleatorio:
    print(f"Parabéns, você acertou o número era {numero_escolhido} mesmo.")
else:
    print(f"Você errou, o número era {numero_aleatorio}")
