import mysql.connector

class BancoDeDados:
    
    def obterConexao(self):
        try:
            self.conexao = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Caio2004$',
                database='biblioteca'
            )
            return self.conexao
        except:
            raise Exception('Não foi possivel conectar ao banco.')
        
    def fecharConexao(self):
        self.conexao.close()
    
    def realizarCommit(self):
        self.conexao.commit()

    def realizarRollback(self):
        self.conexao.rollback()



