from dominio.usuarioServico import UsuarioServico

class UsuarioRepositorioBanco(UsuarioServico):

    def __init__(self, cursor):
        self.cursor = cursor
    
    def cadastrar_usuario():
        pass

    def consultar_usuario(self, usuario):
        sql = "SELECT username FROM usuariotb WHERE username = %s"
        valores = (usuario,)
        
        self.cursor.execute(sql, valores)

        lista_usuario = self.cursor.fetchone()
        
        return lista_usuario
    
    def verificar_usuario_existe(self, usuario):
        lista_usuario = self.consultar_usuarios(usuario)

        if not lista_usuario:
            return 'nao tem nada aqui'
        else:
            return 'achei um usuario'
        
    def consultar_usuarios(self):
        sql = 'SELECT username, password FROM usuariotb'

        self.cursor.execute(sql)

        lista_usuarios = self.cursor.fetchall()

        return lista_usuarios
        
    def autenticar_usuario(self, usuario, senha):
        lista_usuarios = self.consultar_usuarios()
        

        for conta in lista_usuarios:
            if f'{usuario}, {senha}' in f'{conta[0]}, {conta[1]}':
                return True
        
        return False
        




    