from persistencia.banco.leitorRepositorioBanco import LeitorRepositorioBanco
from persistencia.banco.auxiliarBanco import BancoDeDados

class LeitorServicoImpl:

    def __init__(self):
        self.banco = BancoDeDados()
        self.conexao = self.banco.obterConexao()
        self.cursor = self.conexao.cursor()
        self.leitor_repositorio_banco = LeitorRepositorioBanco(self.cursor)

    def cadastrar_leitor(self, leitor_VO):
        self.validar_dados(leitor_VO)

        leitor_existe = self.leitor_repositorio_banco.verificar_leitor_existe(leitor_VO.cpf)

        if leitor_existe == False:
            self.leitor_repositorio_banco.cadastrar_leitor(leitor_VO)
            self.banco.realizarCommit()
            self.banco.fecharConexao()
        else:
            self.banco.realizarRollback()
            self.banco.fecharConexao()
            raise ValueError('Leitor já cadastrado.')

    def obter_leitores(self):
        leitores = self.leitor_repositorio_banco.obter_leitores()

        return leitores
    
    def consultar_leitor(self, cpf):
        leitor_existe = self.leitor_repositorio_banco.verificar_leitor_existe(cpf)

        if leitor_existe == False:
            raise ValueError('Leitor não existe.')
        else: 
            leitor = self.leitor_repositorio_banco.consultar_leitor(cpf)

        return leitor

    
    def atualizar_leitor(self, leitor_VO):
         
        self.validar_dados(leitor_VO)
        
        status = self.leitor_repositorio_banco.verificar_leitor_existe(leitor_VO.cpf)

        if status == True:
            self.leitor_repositorio_banco.atualizar_leitor(leitor_VO)
            self.banco.realizarCommit()
            self.banco.fecharConexao()
        else:
            self.banco.realizarCommit()
            self.banco.fecharConexao()
            raise ValueError('Esse leitor não existe')

    
    def deletar_leitor(self, cpf):
        if len(cpf) != 11:
            raise ValueError('CPF inválido')
        
        leitor = self.leitor_repositorio_banco.verificar_leitor_existe(cpf)

        if leitor == True:
            self.leitor_repositorio_banco.deletar_leitor(cpf)
            self.banco.realizarCommit()
            self.banco.fecharConexao()
        else:
            self.banco.realizarRollback()
            self.banco.fecharConexao()
            raise ValueError('CPF não existe')
        
    def validar_dados(self, leitor_VO):
         
        if len(leitor_VO.cpf) != 11:
            raise ValueError('CPF inválido.')
        if not leitor_VO.cpf.isdigit():
            raise ValueError('CPF invalido')
        if len(leitor_VO.nome) < 1 or len(leitor_VO.nome) > 100:
            raise ValueError('Nome inválido.')
        if not leitor_VO.telefone.isdigit():
            raise ValueError('Telefone invalido')