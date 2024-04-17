# Escreva um programa que imprima os n primeiros números da sequência de Fibonacci.

n = int(input("Digite um número inteiro (n) número da sequência de fibonacci: "))

if n <= 0:
    print(f"Insira um número inteiro positivo")
elif n == 1:
    print(f"O primeiro número da sequência é 0")
else:
    a, b = 0, 1
    soma = 0
    print(f"Os primeiros {n} números da sequência são: ", end="")
    while soma < n:
        print(a, end=' ')
        a, b = b, a + b
        soma += 1
