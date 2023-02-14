cont = 0
while True: #loop infinito
    n = int(input('Quer a tabuada de qual valor: '))
    print('\033[1;33m~\033[m'*25)
    if n < 0:
        break # interrompe o laço ;desviando para fora dele .eu posso escolher o ponto onde ele sera interrompido
    while cont < 10:
        cont = cont + 1
        print(f'{n*1} x {cont} = {n * cont}')
    cont = cont - 10
    print('\033[1;33m~\033[m'*25)
print('PROGRAMA DE TABUADA ENCERRADA. VOLTE SEMPRE')
