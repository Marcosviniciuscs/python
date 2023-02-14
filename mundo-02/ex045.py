from random import randint
from time import sleep
print('{:=^20}'.format('JO KEN PO'))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
escolha = int(input('sua escolha: '))
sleep(0.3)
print('JO')
sleep(0.4)
print('KEN')
sleep(0.5)
print('PO')
pc = randint(0,2)
if escolha == 0:#pedra
    print('o jogador escolheu PEDRA.')
    if pc == 0:
        print('o computadore escolheu PEDRA')
        print('empate')
    elif pc == 1:
        print('o computador escolheu PAPEL')
        print('o computador GANHOU!!')
    elif pc == 2:
        print('o computador escolheu TESOURA')
        print('o jogador VENCEU!!')
if escolha == 1:#papel
    print('o jogador escolheu PAPEL')
    if pc == 0:
        print('o computador escolheu PEDRA')
        print('o jogador VENCEU!!')
    elif pc == 1:
        print('o computador escolheu PAPEL')
        print('Empate')
    elif pc == 2:
        print('o computador escolheu TESOURA')
        print('o computador VENCEU!!')
if escolha == 2:#tesoura
    print('o jogador escolheu TESOURA')
    if pc == 0:
        print('o computador escolheu PEDRA')
        print('o computador VENCEU!!')
    elif pc == 1:
        print('o computador escolheu PAPEL')
        print('o jogador VENCEU!!')
    elif pc == 2:
        print('o computador escolheu TESOURA')
        print('Empate')
