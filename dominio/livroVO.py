class LivroVO:

    def __init__(self, isbn, titulo, autor, genero, quantidade=None, id_livro=None):
        self.id_livro = id_livro
        self.isbn = isbn
        self.titulo = titulo.title()
        self.autor = autor.title()
        self.genero = genero.title()
        self.quantidade = quantidade
        