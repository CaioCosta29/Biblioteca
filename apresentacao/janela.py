from dominio.leitorVO import LeitorVO
from dominio.usuarioVO import UsuarioVO
from dominio.livroVO import LivroVO

from dominio.impl.leitorServiceImpl import LeitorServicoImpl
from dominio.impl.usuarioServiceImpl import UsuarioServicoImpl
from dominio.impl.livroServiceImpl import LivroServiceImpl

from persistencia.arquivo.leitorCRUDArquivo import LeitorCRUDArquivo as LeitorCRUD
from persistencia.arquivo.livroCRUDArquivo import LivroCRUDArquivo as LivroCRUD
from persistencia.arquivo.usuarioArquivo import UsuarioArquivo as Usuario
from persistencia.arquivo.emprestimoCRUDArquivo import EmprestimoCRUDArquivo as EmprestimoCRUD
from apresentacao.utils import *
import getpass

import os

# Sistema para bibliotecas, aonde pode se cadastrar, modificar, visualizar e excluir leitores e livros, além de poder emprestar livros


def exibir_tela_login():
    
    while True:
        print('*** Sistema de Controle de Biblioteca ***\n\n')

        print('Faça o login')
        print('teste')

        username = input('Digite seu usuario: ')
        senha = getpass.getpass('Digite sua senha: ')

        usuario_VO = UsuarioVO(username, senha)

        try:
            teste = UsuarioServicoImpl()
            verificacao_login = teste.autenticar_usuario(usuario_VO)
            if verificacao_login == True:
                exibir_tela_principal()
            else:
                print('\n')
                print('Senha ou usuario invalidos!')

                input('Digite qualquer coisa para continuar')
                os.system('cls')
                continue
        except ValueError as ex:
            print(ex)
            pausar()
            os.system('cls')

        except Exception as xe:
            print(xe)
            pausar()
            os.system('cls')
        

def exibir_tela_principal():
    while True:
        os.system('cls')
        print('*** Sistema de Controle de Biblioteca ***\n\n')

        print('''-------- Menu Principal --------
Digite '1' para entrar na aba de leitor
Digite '2' para entrar na aba de livro
Digite '3' para cadastrar um novo login
Digite '4' para entrar na aba de emprestimo
Digite '5' para encerrar o programa''')
        
        try:
            while True:
                char = get_single_char()
                if char.isdigit():
                    escolha_do_usuario = int(char)
                    break

        except ValueError:
            continue

        match escolha_do_usuario: 
            case 1:
                exibir_tela_leitores()
            
            case 2:
                exibir_tela_livro()
                
            case 3:
                exibir_tela_cadastro_usuario()

            case 4:
                exibir_tela_emprestimo()

            case 5:
                os.system('cls')
                exit('Obrigado por usar o sistema!')
    
def exibir_tela_leitores():

    while True:
        os.system('cls')
        print('*** Sistema de Controle de Biblioteca ***\n\n')
        print('''---------- Leitores ----------
Digite '1' para cadastrar um leitor
Digite '2' para visualizar leitores
Digite '3' para editar um leitor
Digite '4' para excluir um leitor
Digite '5' para voltar ao menu principal''')
        try:
            while True:
                char = get_single_char()
                if char.isdigit():
                    escolha_do_usuario = int(char)
                    break
        except ValueError as ex:
            print(xe)
            continue

        match escolha_do_usuario:
            case 1:
                cpf_leitor = input('\nDigite o CPF do leitor: ')
                nome_leitor = input('Digite o nome do leitor: ')
                telefone_leitor = input('Digite o telefone: ')
                email_leitor = input('Digite o email: ')

                leitorVO = LeitorVO(cpf_leitor, nome_leitor, telefone_leitor, email_leitor)
                
                try: 
                    servico_leitor = LeitorServicoImpl()
                    servico_leitor.cadastrar_leitor(leitorVO)
                    print("\nCadastrado com sucesso!")
                    pausar()
                except ValueError as erro_de_atributo:
                    print(str(erro_de_atributo))
                    pausar()
                
                except Exception as xe:
                    print(f'\nErro não indetificado: {str(xe)}')
                    print(xe)
                    pausar()
                    
            case 2:
                servico_leitor = LeitorServicoImpl()
                leitores = servico_leitor.obter_leitores()
                
                if leitores:
                    for leitor in leitores:
                        print(f'CPF: {leitor.cpf.ljust(20)} | Nome: {leitor.nome.ljust(20)} | Telefone: {leitor.telefone.ljust(20)} | Email: {leitor.email.ljust(20)}')
                else:
                    os.system('cls')
                    print('Não nenhum leitor cadastrado')
                
                input('Aperte qualquer tecla para continuar')
                os.system('cls')

            case 3:
                cpf_atualizar = input('\nDigite o CPF do leitor que deseja atualizar: ')
                
                
                nome_atualizar = input('\nDigite o nome: ')
                telefone_atualizar = input('Digite o telefone: ')
                email_atualizar = input('Digite o email: ')

                leitor_VO = leitorVO(cpf_atualizar, nome_atualizar, telefone_atualizar, email_atualizar)

                try:
                    servico_leitor = LeitorServicoImpl()
                    servico_leitor.atualizar_leitor(leitor_VO)
                    print('\nAtualizado com sucesso')
                    pausar()

                except ValueError as ex:
                    print(ex)
                    
                except Exception as xe:
                    print(xe)

            case 4:
                cpf_excluir = input('\nDigite o CPF do leitor que deseja excluir: ')
                
                try:
                    servico_leitor = LeitorServicoImpl()
                    servico_leitor.deletar_leitor(cpf_excluir)
                    print('\nLeitor excluído com sucesso')
                    pausar()
                except ValueError as ex:
                    print(f'\n{ex}')
                
                pausar()
                os.system('cls')
                
            case 5:
                os.system('cls')
                break
    
def exibir_tela_livro():
    
    while True:
        os.system('cls')
        print('*** Sistema de Controle de Biblioteca ***\n\n')
        print('''---------- Livros ----------
Digite '1' para cadastrar um livro
Digite '2' para visualizar os livros
Digite '3' para atualizar um livro
Digite '4' para excluir um livro
Digite '5' para voltar ao menu principal''')
    
        while True:
                char = get_single_char()
                if char.isdigit():
                    escolha_do_usuario = int(char)
                    break

        match escolha_do_usuario:
            case 1:
                isbn = input('Digite o ISBN do livro: ')
                titulo = input('Digite o titulo do livro: ')
                autor = input('Digite o autor do livro: ')
                genero = input('Digite o genero do livro: ')
                # estoque = int(input('Quantos livros deseja adicionar no estoque'))

                livro_VO = LivroVO(isbn, titulo, autor, genero)
                
                try:
                    servico_livro = LivroServiceImpl()
                    servico_livro.cadastrar_livro(livro_VO)
                    print('\nCadastrado com sucesso')
                    pausar()
                except ValueError as erro:
                    print(erro)
                    pausar()
                except Exception as erro:
                    print(erro)
                    pausar()

            case 2:
                servico_livro = LivroServiceImpl()
                livros = servico_livro.obter_livros()

                if livros:
                    for livro in livros:
                        print(f'ISBN: {livro.isbn.ljust(25)} | Titulo: {livro.titulo.ljust(25)} | Autor: {livro.autor.ljust(25)} | Gênero: {livro.genero.ljust(20)}')
                else:
                    os.system('cls')
                    print('Não existe nenhum livro cadastrado')

                input('Aperte qualquer tecla para continuar')
                os.system('cls')

            case 3:
                isbn_atualizar = input('Digite o ISBN do livro que deseja modificar: ')
                titulo_atualizar = input('Digite o titulo do livro: ')
                autor_atualizar = input('Digite o autor do livro: ')
                genero_atualizar = input('Digite o genero do livro: ')
                
                livro_VO = LivroVO(isbn_atualizar, titulo_atualizar, autor_atualizar, genero_atualizar)

                try:
                    servico_livro = LivroServiceImpl()
                    servico_livro.atualizar_livro(livro_VO)
                    print('Livro atualizado')
                    pausar()
                except ValueError as erro:
                    print(erro)
                except Exception as erro:
                    print(erro)

                os.system('cls')
                

            case 4:
                isbn_excluir = input('Digite o ISBN do livro: ')

                try:
                    servico_livro = LivroServiceImpl()
                    servico_livro.deletar_livro(isbn_excluir)
                    print('Livro removido')
                    pausar()

                except ValueError as erro:
                    print(erro)
                except Exception as erro:
                    print(erro)
                
            case 5:
                os.system('cls')
                break
  
def exibir_tela_cadastro_usuario():
    os.system('cls')
    username = input('Digite o nome do usuario: ')
    senha = input('Digite sua senha: ')
    os.system('cls')

    controle_usuario = Usuario()
    controle_usuario.cadastrar_usuario(username, senha)

def exibir_tela_emprestimo():

    while True:
        os.system('cls')
        print('*** Sistema de Controle de Biblioteca ***\n\n')
        print('''---------- Empréstimo ----------
Digite '1' para emprestar um livro
Digite '2' para devolver um livro
Digite '3' para visualizar livros emprestados
Digite '4' para voltar ao menu principal''')
    
        while True:
                char = get_single_char()
                if char.isdigit():
                    escolha_do_usuario = int(char)
                    break

        match escolha_do_usuario:
            case 1:
                titulo_emprestimo = input('Digite o titulo do livro: ').title()
                autor_emprestimo = input('Digite o autor do livro: ').title()
                nome_leitor_emprestimo = input('Digite o nome do leitor: ').title()

                txt = EmprestimoCRUD.emprestar_livro(titulo_emprestimo, autor_emprestimo, nome_leitor_emprestimo)
                print(txt)

            case 2:
                titulo_devolver = input('Digite o titulo do livro: ').title()
                autor_devolver = input('Digite o autor do livro: ').title()
                nome_leitor_devolver = input('Digite o nome do leitor: ').title()

                txt = EmprestimoCRUD.devolver_livro(titulo_devolver, autor_devolver, nome_leitor_devolver)
                os.system('cls')
                print(txt)
                
            case 3:
                emprestimos = EmprestimoCRUD.visualizar_emprestimos()

                if len(emprestimos) > 0:
                    os.system('cls')
                    for emprestimo in emprestimos:
                        print(f'Titulo: {emprestimo[0].ljust(25)} | Autor: {emprestimo[1].ljust(25)} | Nome do Leitor: {emprestimo[2].ljust(25)}')
                    
                else:
                    print('Não existe nenhum emprestimo')

                input('\nAperte qualquer tecla para continuar')
                os.system('cls')

            case 4:
                os.system('cls')
                break



