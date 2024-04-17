# Escreva um programa que calcule a soma dos números ímpares de 1 a 100.

soma_impares = 0
i = 1

while(i <= 100):
    if i % 2 != 0:
        soma_impares += 1
    i += 1

print(f"A soma dos números ímpares é: {soma_impares}")
