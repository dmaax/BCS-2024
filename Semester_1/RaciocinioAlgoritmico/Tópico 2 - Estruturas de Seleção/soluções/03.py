# Informe o dia da semana a partir de um número entre 1 e 7. Exemplo, 1- Domingo, 2- Segunda etc. Se digitar outro valor deve aparecer “valor inválido”)

numero = int(input("Digite um número entre 1 e 7: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda")
elif numero == 3:
    print("Terça")
elif numero == 4:
    print("Quarta")
elif numero == 5:
    print("Quinta")
elif numero == 6:
    print("Sexta")
elif numero == 7:
    print("Sábado")
else:
    print("Valor inválido")