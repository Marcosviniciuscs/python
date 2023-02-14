from time import sleep
c = ('\033[m',      # 0 sem cor
     '\033[1;41m',  # 1 red
     '\033[1;42m',  # 2 gren
     '\033[1;43m',  # 3 yellow
     '\033[1;44m',  # 4 blue
     '\033[1;45m',  # 5 purple
     '\033[1;46m',  # 6 verde claro
     '\033[1;47m',  # 7 cinza
     '\033[1;48m',  # 8 white
     '\033[7m'      # 9 cor invertida
     )

def titulo(txt,cor=0):
    tam = len(txt)
    print(c[cor], end='')
    print('~'*tam)
    print(txt)
    print('~'*tam)
    print(c[0], end='')

def ajuda(com):
    print(c[9],end='')
    help(com)
    print(c[0],end='')

while True:
    titulo('SISTEMA DE AJUDA EM PYTHON', cor=2)
    comando = str(input('Função ou Biblioteca > '))
    titulo(f'Acessando o manual do comando {comando}', cor=4)
    if comando.upper() == 'FIM':
        sleep(0.5)
        titulo('Ate logo...', cor=1)
        sleep(0.5)
        break
    ajuda(comando)
