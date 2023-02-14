listagem =('lápis',1.75,
        'borracha',2.00,
        'Caderno',15.90,
        'Estojo',25.00,
        'Trasferidor',4.20,
        'Compasso',9.99,
        'Mochila',120.00,
        'Canetas',22.30,
        'Livro',34.90)
print('=-'*30)
print('{:^55}'.format('listagem de preço'))
print('=-'*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0 :
        print('{:.<30}'.format(listagem[pos]),end='')
    else:
        print('{:.>30}'.format(listagem[pos]))


