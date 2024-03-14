# As maçãs custam 0,30 cada se forem compradas menos do que uma dúzia, e 0,25 se forem compradas pelo menos doze.
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra

unidade_maca = 0.3
quantidade_maca = int(input("Digite quantas maçãs você vai comprar: "))

if quantidade_maca < 12 and quantidade_maca >= 1:
    if quantidade_maca == 1:
        preco_final = quantidade_maca * unidade_maca
        print(f"O valor total para {quantidade_maca} maçã é: R$ {preco_final}")
    else:
        preco_final = quantidade_maca * unidade_maca
        print(f"O valor total para {quantidade_maca} maçãs é: R$ {preco_final}")
elif quantidade_maca >= 12:
    unidade_maca = 0.25
    preco_final = quantidade_maca * unidade_maca
    print(f"O valor total para {quantidade_maca} maçãs é: R$ {preco_final}")
else:
    print("Quantidade inválida de maçãs")
    