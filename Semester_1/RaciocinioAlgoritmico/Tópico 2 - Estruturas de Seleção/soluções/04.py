# Informe o maior número entre dois números quaisquer

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if primeiro_numero > segundo_numero:
    print(f"O maior número é: {primeiro_numero}")
elif segundo_numero > primeiro_numero:
    print(f"O maior número é: {segundo_numero}")
else:
    print("Os números são iguais")