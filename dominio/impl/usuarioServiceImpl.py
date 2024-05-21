from persistencia.banco.auxiliarBanco import BancoDeDados
from persistencia.banco.usuarioBanco import UsuarioRepositorioBanco

class UsuarioServicoImpl:

    def __init__(self):
        self.banco = BancoDeDados()
        self.conexao = self.banco.obterConexao()
        self.cursor = self.conexao.cursor()
        self.usuario_repositorio_banco = UsuarioRepositorioBanco(self.cursor)

    def cadastrar_usuario(self, usuario_VO):
        
        if len(usuario_VO.usuario) < 1 or len(usuario_VO.usuario) > 50:
            raise ValueError('Digite novamente o usuario!')
        if len(usuario_VO.senha) < 1 or len(usuario_VO.senha) > 30:
            raise ValueError('Digite novamente sua senha!')
        
        usuario_existe = self.usuario_repositorio_banco.verificar_usuario_existe(usuario_VO.usuario)
        
        

        
        
    def autenticar_usuario(self, usuario_VO):
        if len(usuario_VO.usuario) < 1 or len(usuario_VO.usuario) > 50:
            raise ValueError('Digite novamente o usuario!')
        if len(usuario_VO.senha) < 1 or len(usuario_VO.senha) > 30:
            raise ValueError('Digite novamente sua senha!')
        
        usuario_existe = self.usuario_repositorio_banco.autenticar_usuario(usuario_VO.usuario, usuario_VO.senha)

        self.banco.fecharConexao()

        return usuario_existe
        
        
        
         
        
