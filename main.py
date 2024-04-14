import sys
# sys.path.insert(1,'/dominio/')
# sys.path.insert(1,'/persistencia/')

from dominio.leitorCRUD import LeitorCRUD
from dominio.livroCRUD import LivroCRUD
from dominio.usuario import Usuario


import os


def menu():
    print('''--------Menu--------
Digite '1' para entrar na aba de leitor
Digite '2' para entrar na aba de livro
Digite '3' para cadastrar um novo login
Digite '4' para encerrar o programa''')
    




def main():
    controle_usuario = Usuario()
    

    while True:
        print('Faça o login')
        username = input('Digite seu usuario: ')
        senha = input('Digite sua senha: ')
        
        txt, verificacao_login = controle_usuario.autenticar_usuario(username, senha)
        if verificacao_login == True:
            os.system('cls')
            print(txt)
            break
        else:
            os.system('cls')
            print(txt)
            continue
    
    while True:
        menu()
        try:
            escolha_menu = int(input())
    
            match escolha_menu:
                case 1: # entrar na aba do leitor
                    os.system('cls')
                    print('''----------Leitores----------
Digite '1' para cadastrar um leitor
Digite '2' para visualizar leitores
Digite '3' para editar um leitor
Digite '4' para excluir um leitor''')
                    escolha_leitor = int(input())
                    match escolha_leitor:
                        case 1:
                            nome_leitor = input('Digite o nome do leitor: ')
                            telefone_leitor = input('Digite o telefone: ')
                            email_leitor = input('Digite o email: ')
                            LeitorCRUD(nome_leitor, telefone_leitor, email_leitor).cadastrar_leitor()
                            os.system('cls')

                        case 2:
                            if os.path.exists('cadastro_leitor.txt'):
                                
                                leitores = LeitorCRUD.visualizar_leitores()
                                for leitor in leitores:
                                    print(f'Nome: {leitor[0].ljust(20)} | Telefone: {leitor[1].ljust(20)} | Email: {leitor[2].ljust(20)}')

                            else:
                                print('\nNão existe nenhum leitor cadastrado')
                            
                            input('Aperte qualquer tecla para continuar')
                            os.system('cls')

                        case 3:
                            id_nome = input('Digite o nome do leitor que deseja editar: ').title()
                            id_telefone = input(f'Digite o numero de {id_nome}: ')

                            nome_atualizado = input('Digite o nome do leitor para atualizar: ')
                            telefone_atualizado = input('Digite o telefone para atualizar: ')
                            email_atualizado = input('Digite o email para atualizar: ')
                            if os.path.exists('cadastro_leitor.txt'):
                                txt = LeitorCRUD(nome_atualizado, telefone_atualizado, email_atualizado).atualizar_leitor(id_nome, id_telefone)
                                os.system('cls')
                                print(txt)

                            else:
                                os.system('cls')
                                print('Não existe nenhum leitor cadastrado')
                            
                            

                        case 4:
                            nome_excluir = input('Digite o nome do leitor que deseja excluir: ').title()
                            numero_excluir = input('Digite o numero do leitor: ')

                            if os.path.exists('cadastro_leitor.txt'):
                                txt = LeitorCRUD.deletar_leitor(nome_excluir, numero_excluir)
                                print(txt)

                            else:
                                os.system('cls')
                                print('Não existe nenhum leitor cadastrado')
                            
                
                case 2: # entrar na aba do livro
                    print('''----------livros----------
Digite '1' para cadastrar um livro
Digite '2' para visualizar os livros
Digite '3' para atualizar um livro
Digite '4' para excluir um livro''')
                    escolha_livro = int(input(''))
                    match escolha_livro:
                        case 1:
                            titulo = input('Digite o titulo do livro: ')
                            autor = input('Digite o autor do livro: ')
                            genero = input('Digite o genero do livro: ')

                            LivroCRUD(titulo, autor, genero).cadastrar_livro()
                            os.system('cls')

                        case 2:
                            if os.path.exists('cadastro_livro.txt'):
                                livros = LivroCRUD.visualizar_livros()
                                for livro in livros:
                                    print(f'Titulo: {livro[0].ljust(20)} | Autor: {livro[1].ljust(20)} | Gênero: {livro[2].ljust(20)}')

                            else:
                                print('Nenhum livro foi cadastrado')

                            input('Aperte qualquer tecla para continuar')
                            os.system('cls')

                        
                        case 3:
                            id_titulo = input('Digite o titulo do livro que deseja modificar: ').title()
                            id_autor = input(f'Digite o autor de {id_titulo}: ').title()

                            titulo_atualizado = input('Digite o nome do titulo atualizado: ')
                            autor_atualizado = input('Digite o nome do autor atualizado: ')
                            genero_atualizado = input('Digite o gênero atualizado: ')

                            if os.path.exists('cadastro_livro.txt'):
                                txt = LivroCRUD(titulo_atualizado, autor_atualizado, genero_atualizado).atualizar_livro(id_titulo, id_autor)
                                os.system('cls')
                                print(txt)

                            else:
                                os.system('cls')
                                print('Não existe nenhum livro cadastrado')

                        case 4:
                            titulo_excluir = input('Digite o nome do livro que deseja excluir: ')
                            autor_excluir = input(f'Digite o nome do autor de {titulo_excluir}: ')

                            if os.path.exists('cadastro_livro.txt'):
                                
                                pass

                            else:
                                print('Não existe nenhum livro cadastrado')


                            pass
                    

                case 3: # cadastrar um novo login
                    username = input('Digite o nome do usuario: ')
                    senha = input('Digite sua senha: ')
                    os.system('cls')

                    controle_usuario.cadastrar_usuario(username, senha)
                

                case 4:
                    break

        except ValueError:
            os.system('cls')
            print('Erro, digite um numero valido!')

        





    

    

if __name__ == '__main__':
    main()


