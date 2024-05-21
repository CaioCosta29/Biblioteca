class LeitorVO:

    def __init__(self, cpf, nome, telefone, email):
        self.cpf = cpf
        self.nome = nome.title()
        self.telefone = telefone
        self.email = email