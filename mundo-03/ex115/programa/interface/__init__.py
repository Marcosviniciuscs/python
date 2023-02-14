cores = ('\033[1;30m',#0
         '\033[1;31m',#1 vermelho
         '\033[1;32m',#2 verde
         '\033[1;33m',#3 amarelo
         '\033[1;34m',#4 azul
         '\033[1;35m',#5 roxo
         '\033[m')#6 limpo

def lin():
    print('='*35)


def cabeçalho(msg):
    lin()
    print(f'{msg:^35}')
    lin()

def menu(lista):
    for p, m in enumerate(lista):
        print(f'{cores[3]} {p+1} {cores[6]} - {cores[4]} {m} {cores[6]}')

def validaçãoInt():
    cont = 0
    while True:
        lin()
        try:
            num = int(input(f'{cores[3]}Sua opção: {cores[6]}'))
        except ValueError:
            print(cores[1], 'Erro. Porfavor insira um número inteiro válido!', cores[6])
        except KeyboardInterrupt:
            print(cores[1], 'O Sistema foi interrompido pelo usuário.', cores[6])
            return 3
            break
        else:
            if num > 0 and num <= 3:
                cabeçalho(f"Opção {num}")
                return num
                break
            else:
                print(f"{cores[1]} informe uma opção válida! {cores[6]}")
        cont = cont + 1
        if cont == 2:
            return 0
            break

