import msvcrt

def get_single_char():
    char = msvcrt.getch()
    return char.decode('utf-8')

def pausar():
    get_single_char()