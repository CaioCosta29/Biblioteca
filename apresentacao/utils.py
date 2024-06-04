import msvcrt

def get_single_char():
    char = msvcrt.getch()
    return char.decode('utf-8')

def pausar():
    print('Tecle qualquer coisa para continuar')
    get_single_char()