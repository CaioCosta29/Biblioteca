class LeitorVO:

    def __init__(self, cpf, nome, telefone, email, id_leitor=None):
        self.id_leitor = id_leitor
        self.cpf = cpf
        self.nome = nome.title()
        self.telefone = telefone
        self.email = email