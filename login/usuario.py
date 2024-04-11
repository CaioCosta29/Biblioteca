class Usuario:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def cadastrar_usuario(self):
        with open('cadastro_usuario.txt', 'a') as cad:
            cad.write(f'{self.usuario}&&{self.senha}&&\n')

    
    def visualizar_usuarios(self):
        lista = []
        with open('cadastro_usuario.txt', 'r') as cad:
            usuarios = cad.readlines()
            for usuario in usuarios:
                lista.append(usuario.split('&&'))

            return lista

    def autenticar_usuario(self, nome, senha):
        usuarios = self.visualizar_usuarios()

        for usuario in usuarios:
            if f'{usuario[0]}' == nome and f'{usuario[1]}' == senha:
                verificar_login = True
                return 'Logado com sucesso', verificar_login
            
            else:
                verificar_login = False
                return 'Nome ou senha incorretos', verificar_login

        
         
        