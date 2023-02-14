from random import randint
from time import sleep
from operator import itemgetter
resultado = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in resultado.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)
print('=-'*30)
print(f'  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: jogador {v[0]} com {v[1]}')
