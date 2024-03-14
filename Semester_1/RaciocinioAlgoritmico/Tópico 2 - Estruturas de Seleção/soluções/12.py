# Informe se uma pessoa tem idade para votar a partir de seu ano de nascimento

ano_atual = 2024
ano_nascimento = int(input("Digite seu ano de nascimento: "))

if ano_atual - ano_nascimento >= 16:
    print("Você pode votar")
else:
    print("Você ainda não pode votar")