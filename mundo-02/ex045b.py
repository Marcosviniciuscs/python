from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('''\033[1;33msuas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
jogador = int(input('\033[1;33mQUAL É A SUA JOGADA? \033[m'))
print('\033[1;32mJO')
sleep(0.5)
print('\033[1;33mKEN')
sleep(0.5)
print('\033[1;34mPOO!!\033[m')
print('=+'*15)
print('\033[1;32mo jogador escoheu {}\033[m'.format(itens[jogador])) # esse comando permite que o usuario(jogador) escolha dentro da variavel(itens) as seguintes opçoes: pedra,papel e tesoura.
print('\033[1;33mo computador escolheu {}\033[m'.format(itens[computador]))
print('=+'*15)
print('\033[1;34m')# vai colorir o resultado da condição
if jogador == 0: #jogador escolheu pedra
    if computador == 0:
        print('EMPATE')
    elif computador == 1:
        print('O COMPUTADOR VENCEU!!')
    elif computador == 2:
        print('O JOGADOR VENCEU!!')
    else:
        print('INFORMAÇÂO INVÀLIDA!')
elif jogador == 1: # o jogador escolheu papel
    if computador == 0:
        print('O JOGADOR VENCEU!!')
    elif computador == 1:
        print('EMPATE')
    elif computador == 2:
        print('O COMPUTADOR VENCEU!!')
    else:
        print('INFORMAÇÂO INVÀLIDA')
elif jogador == 2: # o jogador esclheu tesoura
    if  computador == 0:
        print('O COMPUTADOR VENCEU!!')
    elif computador == 1:
        print('O JOGADOR VENCEU!!')
    elif computador == 2:
        print('EMPATE')
    else:
        print('INFORMAÇÃO INVÁLIDA')
sleep(1.0)
print('+'*21,'\033[m')