def leiaint(msg):
    while True:
        try: #tenta fazer isso aqui , se nao:
            n = int(input(msg))
        except ValueError:
            print('\033[1;31mErro.Por favor ,digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário!')
            return 0
        else: #se der certo
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except ValueError:
            print('\033[1;32mErro.por favor insira um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;32mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return n


