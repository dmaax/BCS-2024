# Verifique entre duas pessoas quem tem o maior nome e a mais velha. (DICA, use a função len())

nome1 = input("Pessoa 1, digite seu nome completo: ")
idade1 = int(input("Agora digite sua idade em anos: "))

nome2 = input("Pessoa 2, digite seu nome completo: ")
idade2 = int(input("Agora digite sua idade em anos: "))

if len(nome1) > len(nome2):
    print(f"O maior nome é: {nome1}")
elif len(nome2) > len(nome1):
    print(f"O maior nome é: {nome2}")
else:
    print("Os dois nomes tem o mesmo tamanho")

if idade1 > idade2:
    print(f"A pessoa mais velha é {nome1}")
elif idade2 > idade1:
    print(f"A pessoa mais velha é {nome2}")
else:
    print("As duas pessoas tem a mesma idade")