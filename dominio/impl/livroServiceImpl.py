from persistencia.banco.auxiliarBanco import BancoDeDados
from persistencia.banco.livroRepositorioBanco import LivroRepositorioBanco

class LivroServiceImpl:

    def __init__(self):
        self.banco = BancoDeDados()
        self.conexao = self.banco.obterConexao()
        self.cursor = self.conexao.cursor()
        self.livro_repositorio_banco = LivroRepositorioBanco(self.cursor)

    def cadastrar_livro(self, livro_VO):

        self.validar_dados(livro_VO)
        
        livro_existe = self.livro_repositorio_banco.verificar_livro_existe(livro_VO.isbn)

        if livro_existe == False:
            self.livro_repositorio_banco.cadastrar_livro(livro_VO)
            self.banco.realizarCommit()
            self.banco.fecharConexao()
        else:
            self.banco.realizarRollback()
            self.banco.fecharConexao()
            raise Exception('Livro ja cadastrado')
        
    def obter_livros(self):
        livros = self.livro_repositorio_banco.obter_livros()
        
        return livros
    

    def atualizar_livro(self, livro_VO):

        self.validar_dados(livro_VO)
        
        livro_existe = self.livro_repositorio_banco.verificar_livro_existe(livro_VO.isbn)

        if livro_existe == True:
            self.livro_repositorio_banco.atualizar_livro(livro_VO)
            self.banco.realizarCommit()
            self.banco.fecharConexao()
        else:
            self.banco.realizarRollback()
            self.banco.fecharConexao()
            raise Exception('Esse livro não existe')
        

    def deletar_livro(self, isbn):
        if len(isbn) != 13:
            raise ValueError('ISBN invalido')
        
        livro_existe = self.livro_repositorio_banco.verificar_livro_existe(isbn)

        if livro_existe == True:
            self.livro_repositorio_banco.deletar_livro(isbn)
            self.banco.realizarCommit()
            self.banco.fecharConexao()
        else:
            self.banco.realizarRollback()
            self.banco.fecharConexao()
            raise Exception('Livro não encontrado')

    def validar_dados(livro_VO):

        if len(livro_VO.isbn) != 13:
            raise ValueError('ISBN invalido!')
        if len(livro_VO.titulo) < 1 or len(livro_VO.titulo) > 150:
            raise ValueError('Tamanho do titulo invalido!')
        if len(livro_VO.autor) < 1 or len(livro_VO.autor) > 100:
            raise ValueError('Autor invalido!')
        if len(livro_VO.genero) < 1 or len(livro_VO.genero) > 50:
            raise ValueError('Genero invalido!')
        
        
