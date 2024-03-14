# A partir de três notas de um aluno e informe se ele passou por média (7.0 ou mais)

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"A sua média final é: {media}, portanto você passou")
else:
    print(f"A sua média final é: {media}, portanto você não passou")