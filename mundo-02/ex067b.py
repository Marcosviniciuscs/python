print('TABUADA')
while True:
    n = int(input('Qual tabuada você quer mostrar: '))
    print('-'*25)
    if n < 0:# ou seja ,negativo. o comando break será ativado .
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*25)
print('\033[1mPROGRAMA DE TABUÁDA ENCERRADO. VOLTE SEMPRE!\033[m')
