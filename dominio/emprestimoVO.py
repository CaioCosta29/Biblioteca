class emprestimoVO:
    def __init__(self, livro_VO, leitor_VO, total_dias, data_inicio=None, data_retorno=None):
        self.livro_VO = livro_VO
        self.leitor_VO = leitor_VO
        self.data_inicio = data_inicio
        self.total_dias = total_dias
        self.data_retorno = data_retorno
        