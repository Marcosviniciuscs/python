from random import randint
computador = randint(0, 10)
cont = 0
print('sou seu computador...acabei de pensar em um numero entre 0 e 10.')
print('será que você consegue advinhar qual foi?')
acertou = False
while not acertou:
    jogador = int(input('qual é o seu palpite? '))
    cont = cont + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('menos...tente novamente')
        elif jogador < computador:
            print('mais...tente novamente.')
print('voce acertou com {} palpites'.format(cont))