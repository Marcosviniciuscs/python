dados = {}
numgols = []
s = 0
dados['Nome'] = str(input('Nome do jogador: '))
num = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(0, num):
    numgols.append(int(input(f'Quantos gols na partidas {c}? ')))
dados['gols'] = numgols[:]
for n in numgols:
    s += n
dados['total'] = s
print('=-'*30)
print(dados)
print('=-'*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {dados["Nome"]} jogou {num} partidas.')
for part, gol in enumerate(dados['gols']):
    print(f'  => Na partida {part},fez {gol} gols.')
print(f'Foi um total de {s} gols')
