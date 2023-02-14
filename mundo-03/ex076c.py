lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Trasferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
print('='*58)
print(f'{"Listagem de preço":^58}')
print('='*58)
for item in range(0,len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<50}',end=' ')
    elif item % 2 == 1:
        print(f'{lista[item]:>6.2f}')
print('-'*58)