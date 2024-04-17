from dominio.leitorServico import LeitorServico

class LeitorCRUDBanco(LeitorServico):
    def __init__(self, nome, telefone, email):
        self.nome = nome.title()
        self.telefone = telefone
        self.email = email

    def cadastrar_leitor(self):
        raise NotImplementedError()

    def cadastrar_leitores(leitores):
        raise NotImplementedError()

    def visualizar_leitores():
        raise NotImplementedError()

    def atualizar_leitor(self, id_nome, id_telefone):
        raise NotImplementedError()

    def deletar_leitor(id_nome, id_telefone):
        raise NotImplementedError()
