from persistencia.banco.emprestimoRepositorioBanco import EmprestimoRepositorioBanco
from persistencia.banco.estoqueRepositorioBanco import EstoqueRepositorioBanco

from dominio.impl.estoqueServiceImpl import EstoqueServiceImpl
from dominio.estoqueVO import EstoqueVO

from persistencia.banco.auxiliarBanco import BancoDeDados
import datetime

class EmprestimoServiceImpl:

    def __init__(self):
        self.banco = BancoDeDados()
        self.conexao = self.banco.obterConexao()
        self.cursor = self.conexao.cursor()
        self.emprestimo_repositorio_banco = EmprestimoRepositorioBanco(self.cursor)        

    def realizar_emprestimo(self, emprestimo_VO):
        if int(emprestimo_VO.total_dias) > 15:
            raise ValueError('Maximo de 15 dias permitido')
        if int(emprestimo_VO.total_dias) < 1:
            raise ValueError('Erro no total de dias')
        
        emprestimo_existe = self.emprestimo_repositorio_banco.existe_emprestimo_pendente(emprestimo_VO.leitor_VO.id_leitor, emprestimo_VO.livro_VO.id_livro)

        if emprestimo_existe == True:
            raise ValueError('Já existe um emprestimo em aberto para este leitor')
        
        estoque_repositorio_banco = EstoqueRepositorioBanco(self.cursor)
        livro_disponivel = estoque_repositorio_banco.verificar_livro_disponivel_em_estoque(emprestimo_VO.livro_VO.isbn)

        if livro_disponivel == False:
            raise ValueError('Não existe mais livros disponiveis')

        emprestimo_VO.data_inicio = datetime.datetime.now().date()
        
        try:
            self.emprestimo_repositorio_banco.realizar_emprestimo(emprestimo_VO.leitor_VO.id_leitor, emprestimo_VO.livro_VO.id_livro, emprestimo_VO.data_inicio, emprestimo_VO.total_dias)
            estoque_VO = EstoqueVO(emprestimo_VO.livro_VO, '1')

            estoque_service = EstoqueServiceImpl()
            estoque_service.reduzir_estoque(estoque_VO)

            self.banco.realizarCommit()
            self.banco.fecharConexao()
        
        except:
            self.banco.realizarRollback()
            self.banco.fecharConexao()
            raise ValueError('Erro ao tentar incluir o emprestimo')
        
    def devolver_livro(self, livro_VO, leitor_VO):

        emprestimo_existe = self.emprestimo_repositorio_banco.existe_emprestimo_pendente(leitor_VO.id_leitor, livro_VO.id_livro)

        if emprestimo_existe == False:
            raise ValueError('Livro não está emprestado ao leitor')

        try:
            self.emprestimo_repositorio_banco.devolver_livro(livro_VO, leitor_VO)

            estoque_VO = EstoqueVO(livro_VO, '1')

            estoque_service = EstoqueServiceImpl()
            estoque_service.acrescentar_estoque(estoque_VO)

            self.banco.realizarCommit()
            self.banco.fecharConexao()
        
        except ValueError as erro:
            
            self.banco.realizarRollback()
            self.banco.fecharConexao()
            raise ValueError(f'Erro ao tentar devolver o livro. {erro}')
        
        except Exception as erro:
            
            self.banco.realizarRollback()
            self.banco.fecharConexao()
            raise ValueError(f'Erro ao tentar devolver o livro. {erro}')
        
    def obter_leitores(self):
        emprestimos = self.emprestimo_repositorio_banco.consultar_emprestimos()

        return emprestimos
        

        

        


        