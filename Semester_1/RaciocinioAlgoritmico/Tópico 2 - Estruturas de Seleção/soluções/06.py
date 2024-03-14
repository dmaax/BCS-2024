# Informe se um ano é bissexto ou não.

ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")