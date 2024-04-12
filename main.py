from login.usuario import Usuario
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
        except ValueError:
            os.system('cls')
            print('Digite um numero!')
            continue

        match escolha_menu:
            case 1: # entrar na aba do leitor
                pass

            case 2: # entrar na aba do livro
                pass

            case 3: # cadastrar um novo login
                username = input('Digite o nome do usuario: ')
                senha = input('Digite sua senha: ')
                os.system('cls')

                controle_usuario.cadastrar_usuario(username, senha)
                

            case 4:
                break
        





    

    

if __name__ == '__main__':
    main()


