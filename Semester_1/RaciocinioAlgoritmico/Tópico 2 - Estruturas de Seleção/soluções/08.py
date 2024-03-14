# Informe se um número é múltiplo de um número N qualquer

numero = int(input("Digite um número: "))
multiplo = int(input("Digite outro número: "))

if numero % multiplo == 0:
    print(f"O número {numero} é múltiplo de {multiplo}")
else:
    print(f"O número {numero} não é múltiplo de {multiplo}")