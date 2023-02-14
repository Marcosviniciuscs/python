def linhasverde(txt):
    print('\033[1;42m',end="")
    print('~'*len(txt))
    print(txt)
    print('~'*len(txt))
    print('\033[m',end='')


def linhasazul(txt):
    print('\033[1;44m',end='')
    print('~'*len(txt))
    print(txt)
    print('~'*len(txt))
    print('\033[m',end='')


def comando(txt):
    print('\033[1;40m',end='')
    txt1 = str(input(txt))
    print('\033[m',end='')
    return txt1


def ajuda():
    while True:
        linhasverde('SISTEMA DE AJUDA EM PYHELP')
        txt2 = comando('Função ou Biblioteca> ')
        if txt2.upper() in "FIM":
            print('\033[1;41m',end='')
            print('~'*15)
            print('  Até logo...')
            print('~'*15)
            print('\033[m')
            break
        linhasazul(f'Acessando o manual do comando {txt2}')
        print('\033[7m',end='')
        help(txt2)
        print('\033[m',end='')


ajuda()
