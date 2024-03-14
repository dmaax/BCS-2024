# Informe se uma pessoa pode doar sangue (entre 18 e 59 anos)

idade = int(input("Digite sua idade em anos: "))

if idade >=18 and idade <= 59:
    print(f"Você pode doar sangue pois tem {idade} anos")
else:
    print(f"Você não pode doar sangue pois tem {idade} anos")