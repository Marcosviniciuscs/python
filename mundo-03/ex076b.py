lista = ('lapis', 1.75,
         'Borracha', 2.00,
         'caderno', 15.90,
         'estojo', 25.00,
         'traferidor', 4.20,
         'compasso', 9.99,
         'mochila', 120.32,
         'canetas', 22.30,
         'livro', 34.90
         )
print('-'*57)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*57)
for item in range(0,len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<20}', end='')
    else:
        print(f'{"R$":.>30}{lista[item]:>7.2f}')
print('-'*30)
