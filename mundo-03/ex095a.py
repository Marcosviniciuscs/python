dados = dict()
numgols = list()
time = list()
s = 0
while True:
    dados['nome'] = str(input('Nome: '))
    numpartidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for n in range(0, numpartidas):
        numgols.append(int(input(f'    Quantos gols na {n+1} partidas: ')))
    for valor in numgols:
        s += valor
    dados['gols'] = numgols[:]
    dados['total'] = s
    time.append(dados.copy())
    numgols.clear()
    s = 0
    while True:#validador
        resp = str(input("Quer contiuar? [S/N] ")).upper()
        if resp in "NS":
            break
        print('ERRO.tente com N ou S')

    if resp in "N":#interrompe o cadastro
        break
print('=-'*30)
print("Cod  ",end=" ")
for k in dados.keys():
    print(f"{k:<15}", end=" ")
print()
for c in range(0,len(time)):
    print(f"{c:<3}  ",end=" ")
    for v in time[c].values():
        print(f"{str(v):<15}", end=" ")
    print()
print('=-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador: (999 para interromper) '))
    if busca == 999:
        break
    print('--'*30)
    if busca >= len(time):
        print("ERRO. Esse código não existe na lista.")

    else:
        print(f"Levantamento do jogador {time[busca]['nome']}: ")
        for pos, v in enumerate(time[busca]['gols']):
            print(f"Na {pos+1}º partida ,fez {v} gols")
    print('--'*30)
print("<<< VOLTE SEMPRE >>>")



