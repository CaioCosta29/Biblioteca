from persistencia.banco.auxiliarBanco import BancoDeDados
from persistencia.banco.estoqueRepositorioBanco import EstoqueRepositorioBanco

class EstoqueServiceImpl:
    
    def __init__(self):
        self.banco = BancoDeDados()
        self.conexao = self.banco.obterConexao()
        self.cursor = self.conexao.cursor()
        self.estoque_repositorio_banco = EstoqueRepositorioBanco(self.cursor)

    def acrescentar_estoque(self, estoque_VO):
        if not estoque_VO.quantidade.isdigit():
            raise ValueError('Digite um valor inteiro')
        if int(estoque_VO.quantidade) < 1:
            raise ValueError('Digite valores maiores que 0')

        self.estoque_repositorio_banco.acrescentar_estoque(estoque_VO)
        self.banco.realizarCommit()
        self.banco.fecharConexao()

    def reduzir_estoque(self, estoque_VO):
        if int(estoque_VO.quantidade) < 1:
            raise ValueError('Digite valores maiores que 0')
        
        
        self.estoque_repositorio_banco.reduzir_estoque(estoque_VO)
        self.banco.realizarCommit()
        self.banco.fecharConexao()

