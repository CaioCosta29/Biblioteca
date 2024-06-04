from persistencia.banco.leitorRepositorioBanco import LeitorRepositorioBanco
from dominio.leitorVO import LeitorVO

import datetime

from dominio.emprestimoVO import emprestimoVO

class EmprestimoRepositorioBanco:

    def __init__(self, cursor):
        self.cursor = cursor


    def realizar_emprestimo(self, id_leitor, id_livro, data_atual, total_dias):
        sql = 'INSERT INTO emprestimotb (ID_leitor, ID_livro, data_inicio, total_dias) VALUES (%s, %s, %s, %s)'
        valores = (id_leitor, id_livro, data_atual, total_dias)

        self.cursor.execute(sql, valores)

    def consultar_emprestimos(self):
        sql = "SELECT nome, titulo, data_inicio, IFNULL(data_retorno, 'Sem retorno') FROM emprestimotb emp RIGHT JOIN livrotb liv ON liv.ID_livro = emp.ID_livro INNER JOIN leitortb lei ON lei.ID_leitor = emp.ID_leitor;"
        
        self.cursor.execute(sql)

        emprestimos = self.cursor.fetchall()

        return emprestimos
    
    def existe_emprestimo_pendente(self, id_leitor, id_livro):
        sql =  'SELECT * FROM emprestimotb WHERE ID_leitor = %s AND ID_livro = %s AND data_retorno IS NULL'
        valores = (id_leitor, id_livro)

        self.cursor.execute(sql, valores)

        emprestimo_pendente = self.cursor.fetchall()

        if emprestimo_pendente:
            return True
        else:
            return False
        

    def devolver_livro(self, livro_VO, leitor_VO):
        sql = 'UPDATE emprestimotb SET data_retorno = %s WHERE ID_livro = %s AND ID_leitor = %s'
        valores = (datetime.datetime.now().date(), livro_VO.id_livro, leitor_VO.id_leitor)

        self.cursor.execute(sql, valores)
