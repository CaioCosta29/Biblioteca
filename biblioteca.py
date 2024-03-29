class LivroCRUD:
    def cadastrarLivro(self, titulo, autor, genero, quantidade):

        with open("cadastro_livro.txt", "a") as cad:
            cad.write(f"{titulo}&&{autor}&&{genero}&&{quantidade}&&\n")

    def cadastrarLivros(self, livros):
        with open("cadastro_livro.txt", "w") as cad:
            cad.write("")

        for livro in livros:
            self.cadastrarLivro(livro[0], livro[1], livro[2], livro[3])

    def visualizarLivros(self):
        result = []
        with open("cadastro_livro.txt", "r") as cad:
            livros = cad.readlines()
            for livro in livros:
                result.append(livro.split("&&"))
            
            return result
        
    def visualizarLivro(self, titulo, autor):
       livros = self.visualizarLivros()

       for linha in livros:
           #livroSeparado = linha.split("&&")
           if f"{titulo}, {autor}" in f"{linha[0]}, {linha[1]}":
               return linha
    
    def atualizarLivro(self, id_title, id_autor, title, autor, genero, quantidade):
        livros = self.visualizarLivros()
        encontrado = False
        for linha in livros:
            if f"{id_title}, {id_autor}" in f"{linha[0]}, {linha[1]}":
                encontrado = True
                linha[0] = title
                linha[1] = autor
                linha[2] = genero
                linha[3] = quantidade
                break

        if encontrado:
            self.cadastrarLivros(livros)
            return "Livro encontrado"
        else:
            return "Livro não encontrado"

    def excluirLivro(self, titulo, autor):
        livros = self.visualizarLivros()

        for linha in livros:
            if f"{titulo}, {autor}" in f"{linha[0]}, {linha[1]}":
                livros.remove(linha)
        
        self.cadastrarLivros(livros)

class LeitorCRUD:
    
    def cadastrarLeitor(self, nome, idade, rua, numero, bairro): 
        

        with open("cadastro_leitor.txt", "a") as cad:
            cad.write(f"{nome}&&{idade}&&{rua}&&{numero}&&{bairro}&&\n")

    def cadastrarLeitores(self, leitores=[],):
        with open("cadastro_leitor.txt", "w") as cad:
            cad.write("")
        
        for leitor in leitores: 
            self.cadastrarLeitor(leitor[0], leitor[1],leitor[2], leitor[3], leitor[4])

    def visualizarLeitores(self):
        result = []
        with open("cadastro_leitor.txt", "r") as cad:
            leitores = cad.readlines()
            for leitor in leitores:
                result.append(leitor.split("&&"))   
        return result

    def visualizarLeitor(self, nome):
        leitores = self.visualizarLeitores()
        
        for linha in leitores:
            #leitorSeparado = linha.split()
            if f"{nome}" in linha[0]:
                return linha

    def atualizarLeitor(self, id_nome, nome, idade, rua, numero, bairro):
        encontrado = False
        leitores = self.visualizarLeitores()
        
        
        for linha in leitores:
            if f"{id_nome}" in linha[0]:
                encontrado = True
                linha[0] = nome
                linha[1] = idade
                linha[2] = rua
                linha[3] = numero
                linha[4] = bairro
                break
        
        if encontrado:
            self.cadastrarLeitores(leitores)
            return "Leitor atualizado"
        else:
            return "Leitor não encontrado. Impossível atualizar"

    def excluirLeitor(self, nome):
        leitores = self.visualizarLeitores()
        
        for linha in leitores:
            if f"{nome}" in linha[0]:
                leitores.remove(linha)
        
        self.cadastrarLeitores(leitores)


class EmprestimoCRUD:
    def __init__(self):
        self.leitorControle = LeitorCRUD()
        self.livroControle = LivroCRUD()
        
    def cadastrarEmprestimo(self, nomeCompleto, titulo, autor):
        with open("emprestimo_livro.txt", "a") as cad:
            cad.write(f"{nomeCompleto}&&{titulo}&&{autor}&&\n")

        
    def cadastrarEmprestimos(self, emprestimos=[]):
        with open("emprestimo_livro.txt", "w") as cad:
            cad.write("")
            
            for emprestimo in emprestimos:
                self.cadastrarEmprestimo(emprestimo[0], emprestimo[1], emprestimo[2])
    
    def visualizarEmprestimos(self):
        result = []
        with open("emprestimo_livro.txt", "r") as cad:
            listaEmprestimo = cad.readlines()
            for emprestimo in listaEmprestimo:
                result.append(emprestimo.split("&&"))
            return result

    def emprestarLivro(self, titulo, autor, nome):
        livros = self.livroControle.visualizarLivros()
        leitores = self.leitorControle.visualizarLeitores()


        verificarLeitor = False
        verificarLivro = False


        for item in leitores:
            if f"{nome}" in item:
                
                verificarLeitor = True

        for indice in livros:
            if f"{titulo}, {autor}" in f"{indice[0]}, {indice[1]}":
                
                verificarLivro = True

        if verificarLivro == True and verificarLeitor == True:
            for linha in livros:
                if f"{titulo}, {autor}" in f"{linha[0]}, {linha[1]}":
                    linha[3] = int(linha[3]) - 1
                    
            self.livroControle.cadastrarLivros(livros)
            self.cadastrarEmprestimo(nome, titulo, autor)

        
    def devolverLivro(self, nome, titulo, autor):
        livros = self.livroControle.visualizarLivros()


        listaEmprestimo = self.visualizarEmprestimos()
        
        

        for item in listaEmprestimo: #excluir do arquivo txt
            
            if f"{nome}" in f"{item[0]}" and f"{titulo}" in f"{item[1]}":
                listaEmprestimo.remove(item)
                

                self.cadastrarEmprestimos(listaEmprestimo)

                
                for linha in livros:
                    if f"{titulo}, {autor}" in f"{linha[0]}, {linha[1]}":
                        
                        linha[3] = int(linha[3]) + 1

                self.livroControle.cadastrarLivros(livros)
                

        
    def visualizarDetalhesDoLivroEmprestado(self, nome, titulo, autor):
        emprestimo = self.visualizarEmprestimos()

        for linha in emprestimo:
            #emprestimoSeparado = linha.split("&&")
            if f"{nome}" in linha[0] and f"{titulo}, {autor}" in f"{linha[1]}, {linha[2]}":
                return linha