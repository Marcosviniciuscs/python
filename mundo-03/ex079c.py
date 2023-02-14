lista = []
num = 0
valor = 0
opcao = " "
while True:
    num = int(input('digite um número: '))
    if num not in lista:#"SE O NÚMERO --'NAO ESTIVER' --- DENTRO DA LISTA "
        lista.append(num)
        print('Número adicionado com sucesso!')
    else:
        print('Número duplicado!nao vou adicionar...')
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    while opcao not in 'SN':
        opcao = str(input('valor inválido !quer continuar? [S/N] ')).upper()
    if opcao == 'N':
        break
lista.sort()
print('=-'*30)
print(f'os números adicionados foram: {lista}')
