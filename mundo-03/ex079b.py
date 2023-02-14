num = 0
opcao = ' '
listanum = []
cont = 0
while True:
    num = (int(input('digite um valor: ')))
    cont = cont + 1
    if cont == 1:
        listanum.append(num)
        print('valor adicionado com sucesso...')
    if cont > 1:
        if num in listanum:
            print('Valor duplicado ! tente outro ...')
        elif num not in listanum:
            listanum.append(num)
            print('valor adicionado com sucesso!')
    opcao = str(input('quer continuar? [S/N] ')).upper()
    while opcao not in "SN":
        opcao = str(input('quer continuar? S/N ')).upper()
    if opcao == 'N':
        break
print(f'os valores digitados foram: {sorted(listanum)}')
