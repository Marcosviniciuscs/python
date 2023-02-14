produto = float(input('valor do produto? R$ '))
print('''Escolha a forma de pagamento:
[ 1 ] à vista / cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('sua opção: '))
if opção == 1:  #10% de desconto
    total = produto - (produto * 10 / 100)
    print('voce recebeu 10% de DESCONTO!\nA sua compra custava R${} e com desconto custará R${}'.format(produto,total))
    print('''
    [ 1 ] FINALIZAR COMPRA
    [ 2 ] CANCELAR COMPRA
    ''')
    escolha = int(input('sua opção: '))
    if escolha == 1:
        print('\033[1;32mCompra finalizada!\nMuito obrigado e volte sempre!\033[m')
    elif escolha == 2:
        print('\033[1;31mCompra cancelada!\033[m')
elif opção == 2: #5% de desconto a vista no cartao
    total = produto - (produto * 5 / 100)
    print('voce recebeu 5% DE DESCONTO!\nA sua compra custava R${} e com desconto custará R${}'.format(produto, total))
    print('''
    [ 1 ] FINALIZAR COMPRA
    [ 2 ] CANCELAR COMPRA
    ''')
    escolha = int(input('sua opção: '))
    if escolha == 1:
        print('\033[1;32mCompra finalizada!\nMuito obrigado e volte sempre!\033[m')
    elif escolha == 2:
        print('\033[1;31mCompra cancelada!\033[m')
elif opção == 3: #produto dividido em 2X
    total = produto / 2
    print('preço normal!\nA sua compra  custava R${} dividido em 2X custará R${}.'.format(produto, total))
    print('''
    [ 1 ] FINALIZAR COMPRA
    [ 2 ] CANCELAR COMPRA
    ''')
    escolha = int(input('sua opção: '))
    if escolha == 1:
        print('\033[1;32mCompra finalizada!\nMuito obrigado e volte sempre!\033[m')
    elif escolha == 2:
        print('\033[1;31mCompra cancelada!\033[m')
elif opção == 4: #produto dividido em 3x
    parcelas = int(input('quantas parcelas? '))
    total = produto + (produto * 20 / 100)
    parcjuros = total / parcelas
    print('sua compra será parcelada em {}X de {:.2f}, COM JUROS.'.format(parcelas, parcjuros))
    print('a sua compra de R${} vai custar R${}.'.format(produto, total))
    print('''
    [ 1 ] FINALIZAR COMPRA
    [ 2 ] CANCELAR COMPRA
    ''')
    escolha = int(input('sua opção: '))
    if escolha == 1:
        print('\033[1;32mCompra finalizada!\nMuito obrigado e volte sempre!\033[m')
    elif escolha == 2:
        print('\033[1;31mCompra cancelada!\033[m')
else:
    print('\033[1;31mOPÇÃO INVÀLIDA.TENTE NOVAMENTE\033[m')

