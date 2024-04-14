class LeitorCRUD:
    def __init__(self, nome, telefone, email):
        self.nome = nome.title()
        self.telefone = telefone
        self.email = email
    
    def cadastrar_leitor(self):
        with open('cadastro_leitor.txt', 'a') as cad:
            cad.write(f'{self.nome}&&{self.telefone}&&{self.email}&&\n')

    def cadastrar_leitores(leitores):
        with open('cadastro_leitor.txt', 'w') as cad:
            cad.write('')

        for leitor in leitores:
            LeitorCRUD(leitor[0], leitor[1], leitor[2]).cadastrar_leitor()
    

    def visualizar_leitores():
        lista = []
        with open('cadastro_leitor.txt', 'r') as cad:
            leitores = cad.readlines()

            for leitor in leitores:
               lista.append(leitor.split('&&'))
            
            return lista
        

    def atualizar_leitor(self, id_nome, id_telefone):
        leitores = LeitorCRUD.visualizar_leitores()
        status_encontrado = False

        for linha in leitores:
            
            if f'{id_nome}, {id_telefone}' in f'{linha[0]}, {linha[1]}':
                status_encontrado = True
                linha[0] = self.nome
                linha[1] = self.telefone
                linha[2] = self.email
                break

        if status_encontrado == True:
            LeitorCRUD.cadastrar_leitores(leitores)
            return 'Leitor atualizado'
        else:
            return 'Leitor não encontrado. Impossivel atualizar!'
        
    def deletar_leitor(id_nome, id_telefone):
        leitores = LeitorCRUD.visualizar_leitores()
        print(id_nome, id_telefone)

        for linha in leitores:
            print(linha)
            if f'{id_nome}, {id_telefone}' in f'{linha[0]}, {linha[1]}':
                leitores.remove(linha)
                LeitorCRUD.cadastrar_leitores(leitores)
                return f'Leitor removido com sucesso'
            
            
        return f'Este leitor não está cadastrado'

            
            


        
            
            
