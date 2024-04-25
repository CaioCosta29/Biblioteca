from dominio.emprestioServico import EmprestimoServico
from persistencia.arquivo.leitorCRUDArquivo import LeitorCRUDArquivo as LeitorCRUD
from persistencia.arquivo.livroCRUDArquivo import LivroCRUDArquivo as LivroCRUD

class EmprestimoCRUDArquivo(EmprestimoServico):
    # def __init__(self):
    #     self.livro_controle = LivroCRUD()
    #     self.leitor_controle = LeitorCRUD()

    def cadastrar_emprestimo(titulo, autor, nome_leitor):
        with open('cadastro_emprestimo.txt', 'a') as cad:
            cad.write(f'{titulo}&&{autor}&&{nome_leitor}&&\n')

    def cadastrar_emprestimos(emprestimos):
        with open('cadastro_emprestimo.txt', 'w') as cad:
            cad.write('')

        for emprestimo in emprestimos:
            EmprestimoCRUDArquivo.cadastrar_emprestimo(emprestimo[0], emprestimo[1], emprestimo[2])

    def visualizar_emprestimos():
        lista = []
        with open('cadastro_emprestimo.txt', 'r') as cad:
            emprestimos = cad.readlines()
            for emprestimo in emprestimos:
                lista.append(emprestimo.split('&&'))

            return lista

    def emprestar_livro(titulo, autor, nome_leitor):
        livros = LivroCRUD.visualizar_livros()
        leitores = LeitorCRUD.visualizar_leitores()

        verificar_leitor = False
        verificar_livro = False
        
        for leitor in leitores:
            if f'{nome_leitor}' in leitor:
                verificar_leitor = True
                

        for livro in livros:
            if f'{titulo}, {autor}' in f'{livro[0]}, {livro[1]}':
                verificar_livro = True

        if verificar_livro == True and verificar_leitor == True:
            EmprestimoCRUDArquivo.cadastrar_emprestimo(titulo, autor, nome_leitor)
            return f'Cadastrado com sucesso'

        else:
            return f'Leitor ou livro não encontrado'
        
    
    def devolver_livro(titulo, autor, nome_cliente):
        emprestimos = EmprestimoCRUDArquivo.visualizar_emprestimos()

        for emprestimo in emprestimos:
            if f'{titulo}, {autor}, {nome_cliente}' in f'{emprestimo[0]}, {emprestimo[1]}, {emprestimo[2]}':
                emprestimos.remove(emprestimo)

                EmprestimoCRUDArquivo.cadastrar_emprestimos(emprestimos)
                
            
        
    


