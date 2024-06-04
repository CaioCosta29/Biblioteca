from dominio.leitorRepositorio import LeitorRepositorio
from dominio.leitorVO import LeitorVO

class LeitorRepositorioBanco(LeitorRepositorio):

    def __init__(self, cursor):
        self.cursor = cursor

    def cadastrar_leitor(self, leitorVO):
        sql = "INSERT INTO leitortb (CPF, NOME, TELEFONE, EMAIL) VALUES (%s, %s, %s, %s)"
        valores = (leitorVO.cpf, leitorVO.nome, leitorVO.telefone, leitorVO.email)

        try:
            self.cursor.execute(sql, valores)
        except:
            raise Exception('Erro ao incluir um registro no Banco.')

    def consultar_leitor(self, cpf):
        sql = '''SELECT * FROM leitortb where cpf = %s'''
        valores = (cpf,)

        self.cursor.execute(sql, valores)

        leitor = self.cursor.fetchone()
        
        if leitor:
            leitor_VO = LeitorVO(leitor[1], leitor[2], leitor[3], leitor[4], leitor[0])

            return leitor_VO

    def verificar_leitor_existe(self, cpf):
        leitor = self.consultar_leitor(cpf)
        if not leitor:
            return False
        else:
            return True
        
    def obter_leitores(self):
        sql = 'SELECT * FROM leitortb ORDER BY nome'

        self.cursor.execute(sql)

        leitores = self.cursor.fetchall()
        leitor_retorno = []

        if leitores:
            for leitor in leitores:
                leitorVO = LeitorVO(leitor[1], leitor[2], leitor[3], leitor[4])
                leitor_retorno.append(leitorVO)
            
        return leitor_retorno
        
    
    def atualizar_leitor(self, leitor_VO):
        sql = "UPDATE leitortb SET nome= %s, telefone= %s, email= %s WHERE cpf = %s"
        valores = (leitor_VO.nome, leitor_VO.telefone, leitor_VO.email, leitor_VO.cpf)

        self.cursor.execute(sql, valores)
        

    def deletar_leitor(self, cpf):
        sql = 'DELETE FROM leitortb WHERE cpf = %s'
        valores = (cpf,)

        self.cursor.execute(sql, valores)

              
