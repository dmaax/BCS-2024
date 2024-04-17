# Escreva um programa que solicite um número inteiro e informe se ele é primo ou não.

numero = int(input("Digite um número: "))

flag = False

if numero == 1:
    print(f"O número {numero} não é primo")
elif numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            flag = True
            break

    if flag:
        print(f"O número {numero} não é primo")
    else:
        print(f"O número {numero} é primo")
