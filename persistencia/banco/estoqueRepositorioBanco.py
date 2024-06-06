class EstoqueRepositorioBanco:

    def __init__(self, cursor):
        self.cursor = cursor

    def verificar_livro_disponivel_em_estoque(self, isbn):
        livro_cadastrado_em_estoque = self.verificar_livro_cadastrado_em_estoque(isbn)

        if livro_cadastrado_em_estoque == False:
            return False
        else:
            quantidade_em_estoque = self.obter_quantidade(isbn)
            if quantidade_em_estoque[0] > 0:
                return True
            else: 
                return False

    def verificar_livro_cadastrado_em_estoque(self, isbn):
        sql = 'SELECT * FROM estoquetb INNER JOIN livrotb ON estoquetb.ID_livro = livrotb.ID_livro WHERE isbn = %s'
        valores = (isbn,)

        self.cursor.execute(sql, valores)

        livro_existente_em_estoque = self.cursor.fetchall()
        
        if livro_existente_em_estoque:
            return True
        else:
            return False

    def obter_quantidade(self, isbn):
        sql = 'SELECT quantidade FROM estoquetb RIGHT JOIN livrotb ON estoquetb.ID_livro = livrotb.ID_livro WHERE isbn = %s'
        valores = (isbn,)

        self.cursor.execute(sql, valores)

        quantidade = self.cursor.fetchone()
        
        return quantidade
    
    def acrescentar_estoque(self, estoque_VO):
        livro_cadastrado_em_estoque = self.verificar_livro_cadastrado_em_estoque(estoque_VO.livro_VO.isbn)
        
        if livro_cadastrado_em_estoque == False:
            sql = 'INSERT INTO estoquetb (ID_livro, quantidade) VALUES (%s, %s)'
            valores = (estoque_VO.livro_VO.id_livro, estoque_VO.quantidade)
            
            self.cursor.execute(sql, valores)
        
        else:
            quantidade_em_estoque = self.obter_quantidade(estoque_VO.livro_VO.isbn)

            sql = 'UPDATE estoquetb SET quantidade = %s WHERE ID_livro = %s'
            valores = (quantidade_em_estoque[0] + int(estoque_VO.quantidade), estoque_VO.livro_VO.id_livro)

            self.cursor.execute(sql, valores)

    def reduzir_estoque(self, estoque_VO):
        livro_existe_em_estoque = self.verificar_livro_cadastrado_em_estoque(estoque_VO.livro_VO.isbn)
        
        

        if livro_existe_em_estoque == False:
            raise ValueError('Livro solicitado não existe no estoque')
        
        else:
            quantidade_em_estoque = self.obter_quantidade(estoque_VO.livro_VO.isbn)

            if quantidade_em_estoque[0] - int(estoque_VO.quantidade) < 0:
                raise ValueError('Erro ao tentar retirar mais livros do que possui')

            sql = 'UPDATE estoquetb SET quantidade = %s WHERE ID_livro = %s'
            
            valores = (quantidade_em_estoque[0] - int(estoque_VO.quantidade), estoque_VO.livro_VO.id_livro)

            self.cursor.execute(sql, valores)
        
        
