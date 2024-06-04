import bcrypt

class UsuarioRepositorioBanco:

    def __init__(self, cursor):
        self.cursor = cursor
    
    def cadastrar_usuario(self, usuario_VO):
        sql = "INSERT INTO usuariotb (username, password) VALUES (%s, %s)"
        valores = (usuario_VO.usuario, UsuarioRepositorioBanco.criptografar_senha(usuario_VO.senha))

        self.cursor.execute(sql, valores)
    
    def verificar_usuario_existe(self, usuario):
        lista_usuario = self.consultar_usuario(usuario)

        if lista_usuario:
            return True
        else:
            return False
        
    def consultar_usuario(self, usuario):
        sql = 'SELECT username, password FROM usuariotb WHERE username = %s'
        valores = (usuario,)

        self.cursor.execute(sql, valores)

        lista_usuarios = self.cursor.fetchone()

        return lista_usuarios
        
    def autenticar_usuario(self, usuario, senha):
        lista_usuario = self.consultar_usuario(usuario)
        
        if lista_usuario:
            return UsuarioRepositorioBanco.verificar_senha(senha, lista_usuario[1])
        else:   
            return False
        
    def criptografar_senha(senha):
        bytes = senha.encode('utf-8')
        hashed = bcrypt.hashpw(bytes, bcrypt.gensalt(14))
        return hashed
        

    def verificar_senha(senha, hashed):
        return bcrypt.checkpw(senha.encode('utf-8'), hashed.encode('utf-8'))
        
        




    