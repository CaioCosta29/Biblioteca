from dominio.livroServico import LivroServico
from dominio.livroVO import LivroVO

class LivroRepositorioBanco(LivroServico):
    
    def __init__(self, cursor):
        self.cursor = cursor
        

    def cadastrar_livro(self, livro_VO):
        sql = "INSERT INTO livrotb (isbn, titulo, autor, genero) VALUES (%s, %s, %s, %s)"
        valores = (livro_VO.isbn, livro_VO.titulo, livro_VO.autor, livro_VO.genero)

        self.cursor.execute(sql, valores)
            
    def consultar_livro(self, isbn):
        sql = "SELECT * FROM livrotb WHERE isbn = %s"
        valores = (isbn,)
        
        self.cursor.execute(sql, valores)
        livro = self.cursor.fetchone()

        return livro

    def verificar_livro_existe(self, isbn):
        livro = self.consultar_livro(isbn)

        if livro:
            return True
        else:
            return False
        

    def obter_livros(self):
        sql = "SELECT * from livrotb ORDER BY titulo"

        self.cursor.execute(sql)
        livros = self.cursor.fetchall()
        livros_retorno = []

        if livros:
            for livro in livros:
                livro_VO = LivroVO(livro[1], livro[2], livro[3], livro[4])
                livros_retorno.append(livro_VO)

        return livros_retorno

    def excluir_livro():
        pass

    def atualizar_livro(self, livro_VO):
        sql = "UPDATE livrotb SET titulo = %s, autor = %s, genero = %s WHERE isbn = %s"
        valores = (livro_VO.titulo, livro_VO.autor, livro_VO.genero, livro_VO.isbn)

        self.cursor.execute(sql, valores)

    def deletar_livro(self, isbn):
        sql = "DELETE FROM livrotb WHERE isbn = %s"
        valores = (isbn,)

        self.cursor.execute(sql, valores)

