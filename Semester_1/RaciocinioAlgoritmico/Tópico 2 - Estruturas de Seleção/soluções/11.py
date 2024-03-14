# Peça o login e senha de uma pessoa e informe se o login é valido.

usuario = input("Digite seu nome de usuário: ")
senha = input("Agora digite sua senha: ")

usuario_correto = 'dmaax'
senha_correta = 'Cyb3rS3cFTW'

if usuario == usuario_correto and senha == senha_correta:
    print("Login válido!")
else:
    print("Erro, verifique seu usuário ou senha e tente novamente")