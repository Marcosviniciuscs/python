from random import randint
from time import sleep
cont = 0
computador = randint(0,10)
print('Estou pensando em um numero...')
sleep(1.5)
print('ja pensei !tente acertar.')
jogador = int(input('pense um número: '))
while jogador != computador:#enquanto o jogador for diferente do computador ,o laço ficará repetindo,porque a logica e verdadeira.quando os dados forem iguas,sai do loop ,pois o resultado é falso e executa o ultimo comando.
    if jogador > computador:
        print('menos...tente mais uma vez!')
    elif jogador < computador:
        print('mais...tente mais uma vez!')
    jogador = int(input('pense em outro: '))
    cont = cont + 1    #o contador esta contando quantas vezes o jogador e diferente do computador(while)
print('\033[1;34mPARABÉNS !!  ACERTOU!!\033[m\nvoce escolheu o numero {} e computador escolheu tambem numero {}.'.format(jogador,computador))
print('Voce precisou de {} palpites para acertar.'.format(cont + 1))
