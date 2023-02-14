from operator import itemgetter
jogador = dict()
cadastro = list()
numgols = list()
soma = 0
while True:
    jogador.clear()
    numgols.clear()
    soma = 0
    jogador['nome'] = str(input('Nome: ')) # valor adicionado no dicionário
    num = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, num):
        numgols.append(int(input(f'    Quantos gols marcados na partida {c+1}? ')))
    jogador['gols'] = numgols[:] # valor adicionado no dicionário
    for n in numgols:#total de gols
        soma += n
    jogador['total'] = soma # valor adicionado no dicionário
    cadastro.append(jogador.copy())

    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    while resp not in "SN":
        resp = str(input("Erro.informe S ou N: ")).upper()[0]
    if resp in "N":
        break
print("=-"*30)
print('cod',end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=" ")
print()
print("--"*30)
for p, v in enumerate(cadastro):
    print(f"{p:<3}", end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end=' ')
    print()
while True:
    n = int(input('Mostrar dados de qual jogador?(999 para interromper): '))
    print("--"*30)
    if n == 999:
        break
    if n >= len(cadastro):
        print("ERRO. Não existe esse jogador na lista.")
    else:
        print(f' --  Levantamento do jogador {cadastro[n]["nome"]}:')
        for pos, n in enumerate(cadastro[n]['gols']):
            print(f"No jogo {pos+1}  fez {n} gols.")
    print("--"*30)
print("<< ENCERRADO >>")

