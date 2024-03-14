# Informe se a pessoa digitou uma vogal ou consoante

letra = input("Digite uma letra: ")

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("Vogal")
else:
    print("Consoante")