from dominio.leitorVO import LeitorVO

class LeitorRepositorio:

    def cadastrar_leitor(leitorVO):
        raise NotImplementedError()

    def cadastrar_leitores(leitores):
        raise NotImplementedError()

    def consultar_leitor(cpf):
        raise NotImplementedError()

    def visualizar_leitores():
        raise NotImplementedError()

    def atualizar_leitor(self, id_nome, id_telefone):
        raise NotImplementedError()

    def deletar_leitor(id_nome, id_telefone):
        raise NotImplementedError()