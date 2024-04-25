from dominio.livroServico import LivroServico

class LivroCRUDArquivo(LivroServico):
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo.title()
        self.autor = autor.title()
        self.genero = genero.title()

    def cadastrar_livro(self):
        with open('cadastro_livro.txt', 'a') as cad:
            cad.write(f'{self.titulo}&&{self.autor}&&{self.genero}&&\n')

    def cadastrar_livros(livros):
        with open('cadastro_livro.txt', 'w') as cad:
            cad.write('')

        for livro in livros:
            LivroCRUDArquivo(livro[0], livro[1], livro[2]).cadastrar_livro()


    def visualizar_livros():
        lista = []
        with open('cadastro_livro.txt', 'r') as cad:
            livros = cad.readlines()

            for livro in livros:
                lista.append(livro.split('&&')) 

            return lista
        
    def atualizar_livro(self, id_titulo, id_autor):
        livros = LivroCRUDArquivo.visualizar_livros()
        status_encontrado = False

        for linha in livros:
            if f'{id_titulo}, {id_autor}' in f'{linha[0]}, {linha[1]}':
                status_encontrado = True
                linha[0] = self.titulo
                linha[1] = self.autor
                linha[2] = self.genero

        if status_encontrado == True:
            LivroCRUDArquivo.cadastrar_livros(livros)
            return 'Livro atualizado'
        else:
            return 'Livro não encontrado. Impossivel atualizar!'
        
    def excluir_livro(id_titulo, id_autor):
        livros = LivroCRUDArquivo.visualizar_livros()

        for livro in livros:
            if f'{id_titulo}, {id_autor}' in f'{livro[0]}, {livro[1]}':
                livros.remove(livro)
                LivroCRUDArquivo.cadastrar_livros(livros)
                return f'Livro removido com sucesso'
            
        return f'Este livro não esta cadastrado'
            
           
        
        


