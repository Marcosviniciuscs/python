from random import randint
cont = 0
while True:
    numjogador = int(input('escolha um número: '))
    numcomputador = randint(1, 10)
    soma = numjogador + numcomputador
    opções = ' '
    while opções not in 'PI': #enquanto a valor da variavel nao for/não tiver ' pi',ele vai repetir(validação de dados )
        opções = str(input('Par ou Impar [P/I]')).strip().upper()[0]
    computador = ' '
    resultado = ' '
    if opções == 'P':
        computador = 'IMPAR'
        opções = 'PAR'
        if soma % 2 == 0:
            resultado = 'JOGADOR VENCEU!'
            cont = cont + 1
        elif soma % 2 == 1:
            resultado = 'COMPUTADOR VENCEU!'
    if opções == 'I':
        computador = 'PAR'
        opções = 'ÌMPAR'
        if soma % 2 == 0:
            resultado = 'COMPUTADOR VENCEU!'
        elif soma % 2 == 1:
            resultado = 'JOGADOR VENCEU'
            cont = cont + 1
    print('\033[1m=\033[m'*30)
    print(f'o jogador jogou {numjogador} e escolheu {opções}')
    print(f'o computador jogou {numcomputador} e escolheu {computador}')
    print('-'*30)
    print(f'o total é {soma}','deu PAR' if soma % 2 == 0 else 'deu ÌMPAR')
    print('\033[1;34m', resultado, '\033[m')
    print('\033[1m=\033[m'*30)
    if 'COMPUTADOR VENCEU!' in resultado:
        break
print(f'Você teve {cont} vitorias consecutivas')

