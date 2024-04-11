from login import usuario

while True:
    nome = input('Digite seu nome para cadastro: ')
    senha = input('Digite a senha: ')

    controle_usuario = usuario.Usuario(nome, senha)
    controle_usuario.cadastrar_usuario()
    print(controle_usuario.visualizar_usuarios())
    termo1, termo2 = controle_usuario.autenticar_usuario('eduard','321')
    print(termo1)
    print(termo2)


