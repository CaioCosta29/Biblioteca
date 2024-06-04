from dominio.leitorVO import LeitorVO
from dominio.usuarioVO import UsuarioVO
from dominio.livroVO import LivroVO
from dominio.emprestimoVO import emprestimoVO
from dominio.estoqueVO import EstoqueVO

from dominio.impl.leitorServiceImpl import LeitorServicoImpl
from dominio.impl.usuarioServiceImpl import UsuarioServicoImpl
from dominio.impl.livroServiceImpl import LivroServiceImpl
from dominio.impl.emprestimoServiceImpl import EmprestimoServiceImpl
from dominio.impl.estoqueServiceImpl import EstoqueServiceImpl

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

        username = input('Digite seu usuario: ')
        senha = getpass.getpass('Digite sua senha: ')

        usuario_VO = UsuarioVO(username, senha)

        try:
            usuario_service = UsuarioServicoImpl()
            verificacao_login = usuario_service.autenticar_usuario(usuario_VO)
            if verificacao_login == True:
                exibir_tela_principal()
            else:
                print('\n')
                print('Senha ou usuario invalidos!')

                pausar()
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
Digite '0' para encerrar o programa''')
        
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

            case 0:
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
Digite '0' para voltar ao menu principal''')
        try:
            while True:
                char = get_single_char()
                if char.isdigit():
                    escolha_do_usuario = int(char)
                    break
        except ValueError as ex:
            print(ex)
            continue

        print('')
        match escolha_do_usuario:
            case 1:
                cpf_leitor = input('Digite o CPF do leitor: ')
                nome_leitor = input('Digite o nome do leitor: ')
                telefone_leitor = input('Digite o telefone: ')
                email_leitor = input('Digite o email: ')

                leitorVO = LeitorVO(cpf_leitor, nome_leitor, telefone_leitor, email_leitor)
                
                print('')
                try: 
                    servico_leitor = LeitorServicoImpl()
                    servico_leitor.cadastrar_leitor(leitorVO)
                    print("Cadastrado com sucesso!")
        
                except ValueError as erro_de_atributo:
                    print(str(erro_de_atributo))
                
                except Exception as xe:
                    print(f'Erro não indetificado: {str(xe)}')
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
                
                print('')
                pausar()
                os.system('cls')

            case 3:
                cpf_atualizar = input('Digite o CPF do leitor que deseja atualizar: ')
                nome_atualizar = input('Digite o nome: ')
                telefone_atualizar = input('Digite o telefone: ')
                email_atualizar = input('Digite o email: ')

                leitor_VO = LeitorVO(cpf_atualizar, nome_atualizar, telefone_atualizar, email_atualizar)

                print('')
                try:
                    servico_leitor = LeitorServicoImpl()
                    servico_leitor.atualizar_leitor(leitor_VO)
                    print('Atualizado com sucesso')

                except ValueError as ex:
                    print(ex)
                    
                except Exception as xe:
                    print(xe)

                pausar()

            case 4:
                cpf_excluir = input('Digite o CPF do leitor que deseja excluir: ')
                
                print('')
                try:
                    servico_leitor = LeitorServicoImpl()
                    servico_leitor.deletar_leitor(cpf_excluir)

                    print('Leitor excluído com sucesso')

                except ValueError as ex:
                    print(f'{ex}')
                
                pausar()
                os.system('cls')
                
            case 0:
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
Digite '5' para alterar o estoque
Digite '0' para voltar ao menu principal''')
    
        while True:
                char = get_single_char()
                if char.isdigit():
                    escolha_do_usuario = int(char)
                    break

        print('')
        match escolha_do_usuario:
            case 1:
                isbn = input('Digite o ISBN do livro: ')
                titulo = input('Digite o titulo do livro: ')
                autor = input('Digite o autor do livro: ')
                genero = input('Digite o genero do livro: ')
                # estoque = int(input('Quantos livros deseja adicionar no estoque'))

                livro_VO = LivroVO(isbn, titulo, autor, genero)
                print('')

                try:
                    servico_livro = LivroServiceImpl()
                    servico_livro.cadastrar_livro(livro_VO)
                    print('Cadastrado com sucesso')
                    
                except ValueError as erro:
                    print(erro)

                except Exception as erro:
                    print(erro)
                
                pausar()

            case 2:
                servico_livro = LivroServiceImpl()
                livros = servico_livro.obter_livros()

                if livros:
                    for livro in livros:
                        print(f'ISBN: {livro.isbn.ljust(15)} | Titulo: {livro.titulo.ljust(25)} | Autor: {livro.autor.ljust(25)} | Gênero: {livro.genero.ljust(20)} | Estoque: {str(livro.quantidade).ljust(15)}')
                else:
                    os.system('cls')
                    print('Não existe nenhum livro cadastrado')

                print('')
                pausar()
                os.system('cls')

            case 3:
                isbn_atualizar = input('Digite o ISBN do livro que deseja modificar: ')
                titulo_atualizar = input('Digite o titulo do livro: ')
                autor_atualizar = input('Digite o autor do livro: ')
                genero_atualizar = input('Digite o genero do livro: ')
                
                livro_VO = LivroVO(isbn_atualizar, titulo_atualizar, autor_atualizar, genero_atualizar)

                print('')
                try:
                    servico_livro = LivroServiceImpl()
                    servico_livro.atualizar_livro(livro_VO)
                    print('Livro atualizado')

                except ValueError as erro:
                    print(erro)

                except Exception as erro:
                    print(erro)

                pausar()
                os.system('cls')
                

            case 4:
                isbn_excluir = input('Digite o ISBN do livro: ')

                print('')
                try:
                    servico_livro = LivroServiceImpl()
                    servico_livro.deletar_livro(isbn_excluir)
                    
                    print('Livro removido')

                except ValueError as erro:
                    print(erro)

                except Exception as erro:
                    print(erro)
                
                pausar()
            
            case 5:
                exibir_tela_estoque()

            case 0:
                os.system('cls')
                break
  
def exibir_tela_cadastro_usuario():
    
    while True:
        os.system('cls')

        username = input('Digite o nome do usuario: ')
        senha = input('Digite sua senha: ')

        usuario_VO = UsuarioVO(username, senha)

        print('')
        try:
            usuario_service = UsuarioServicoImpl()
            usuario_service.cadastrar_usuario(usuario_VO)
            
            print('Usuario cadastrado com sucesso')

        except ValueError as erro:
            print(erro)

        except Exception as xe:
            print(f'Erro não indetificado {xe}')

        print('')
        pausar()
        break

def exibir_tela_emprestimo():

    while True:
        os.system('cls')
        print('*** Sistema de Controle de Biblioteca ***\n\n')
        print('''---------- Empréstimo ----------
Digite '1' para emprestar um livro
Digite '2' para devolver um livro
Digite '3' para visualizar livros emprestados
Digite '0' para voltar ao menu principal''')
    
        while True:
                char = get_single_char()
                if char.isdigit():
                    escolha_do_usuario = int(char)
                    break

        print('')
        match escolha_do_usuario:
            case 1:
                isbn_livro = input('Digite o ISBN do livro: ')
                cpf_leitor = input('Digite o CPF do leitor: ')

                print('')

                try:
                    servico_livro = LivroServiceImpl()
                    livro_VO = servico_livro.consultar_livro(isbn_livro)
                    print(f'Titulo: {livro_VO.titulo}')

                    servico_leitor = LeitorServicoImpl()
                    leitor_VO = servico_leitor.consultar_leitor(cpf_leitor)
                    print(f'Nome: {leitor_VO.nome}')

                    print('')

                    total_dias = input('Informe o total de dias (Maximo de 15 dias): ')

                    print('')

                    confirmar = input("Digite 's' para confirmar o emprestimo e 'n' para cancelar: ")

                    print('')

                    if confirmar.lower() == 's':
                        emprestimo_VO = emprestimoVO(livro_VO, leitor_VO, total_dias)

                        emprestimo_service = EmprestimoServiceImpl()
                        emprestimo_service.realizar_emprestimo(emprestimo_VO)

                        print('Livro emprestado com sucesso')

                    else:
                        continue


                except ValueError as erro:
                    print(erro)

                except Exception as erro:
                    print(f'Erro não identificado {erro}')

                print('')   
                pausar()

            case 2:

                isbn_livro = input('Digite o ISBN do livro: ')
                cpf_leitor = input('Digite o CPF do leitor: ')

                print('')
                try:
                    servico_livro = LivroServiceImpl()
                    livro_VO = servico_livro.consultar_livro(isbn_livro)
                    print(f'Titulo: {livro_VO.titulo}')

                    servico_leitor = LeitorServicoImpl()
                    leitor_VO = servico_leitor.consultar_leitor(cpf_leitor)
                    print(f'Nome: {leitor_VO.nome}')

                    print('')

                    confirmar = input("Digite 's' para confirmar o emprestimo e 'n' para cancelar: ")

                    print('')

                    if confirmar.lower() == 's':
                        emprestimo_service = EmprestimoServiceImpl()
                        emprestimo_service.devolver_livro(livro_VO, leitor_VO)

                        print('Livro devolvido com sucesso')

                except ValueError as erro:
                    print(erro)

                except Exception as erro:
                    print(f'Erro não identificado {erro}')

                print('')
                pausar()
                
            case 3:
                emprestimo_service = EmprestimoServiceImpl()
                emprestimos = emprestimo_service.obter_leitores()
                
                if emprestimos:
                    for emprestimo in emprestimos:
                        print(f'Nome: {emprestimo[0].ljust(25)} | Titulo: {emprestimo[1].ljust(25)} | Data do emprestimo: {str(emprestimo[2]).ljust(25)} | Data retorno: {str(emprestimo[3]).ljust(25)}')

                else:
                    print('Não existe livros emprestados')

                print('')
                pausar()
            case 0:
                os.system('cls')
                break

def exibir_tela_estoque():
    while True:
        os.system('cls')
        print("""----------Estoque---------
Digite '1' para acrescentar no estoque
Digite '2' para reduzir no estoque
Digite '0' para voltar
""")
        try:
            while True:
                char = get_single_char()
                if char.isdigit():
                    escolha_do_usuario = int(char)
                    break
        except ValueError as erro:
            print(erro)
            continue

        match escolha_do_usuario:

            case 1:
                try:
                    isbn_livro = input('Digite o ISBN do livro que deseja acrescentar: ')

                    service_livro = LivroServiceImpl()
                    livro_VO = service_livro.consultar_livro(isbn_livro)

                    print(f'Titulo: {livro_VO.titulo}')
                    print('')

                    quantidade = input('Digite a quantidade de livros que deseja adicionar: ')

                    estoque_VO = EstoqueVO(livro_VO, quantidade)

                    estoque_service = EstoqueServiceImpl()
                    estoque_service.acrescentar_estoque(estoque_VO)

                    print('Quantidade acrescentada com sucesso')

                except ValueError as erro:
                    print(erro)

                except Exception as erro:
                    print(f'Erro não identificado {erro}')
                
                print('')
                pausar()

            case 2:
                try:
                    isbn_livro = input('Digite o ISBN do livro que deseja reduzir: ')

                    service_livro = LivroServiceImpl()
                    livro_VO = service_livro.consultar_livro(isbn_livro)

                    print(f'Titulo: {livro_VO.titulo}')
                    print('')

                    quantidade = input('Digite a quantidade de livros que deseja diminuir: ')

                    estoque_VO = EstoqueVO(livro_VO, quantidade)

                    estoque_service = EstoqueServiceImpl()
                    estoque_service.reduzir_estoque(estoque_VO)

                    print('Quantidade reduzida com sucesso')
                
                except ValueError as erro:
                    print(erro)

                except Exception as erro:
                    print(f'Erro não identificado {erro}')

                print('')
                pausar()
            case 0:
                break

                



