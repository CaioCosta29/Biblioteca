from dominio.usuarioServico import UsuarioServico

class UsuarioArquivo(UsuarioServico):
    
    def cadastrar_usuario(self, usuario, senha):
        with open('cadastro_usuario.txt', 'a') as cad:
            cad.write(f'{usuario}&&{senha}&&\n')

    
    def visualizar_usuarios(self):
        lista = []
        with open('cadastro_usuario.txt', 'r') as cad:
            usuarios = cad.readlines()
            for usuario in usuarios:
                lista.append(usuario.split('&&'))
            
            return lista

    def autenticar_usuario(self, usuario, senha):
        usuarios = self.visualizar_usuarios()
        
        for linha in usuarios:
            if f'{linha[0]}' == usuario and f'{linha[1]}' == senha:
                return 'Logado com sucesso', True
                
        return 'Nome ou senha incorretos', False

        
         
        