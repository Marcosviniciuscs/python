num = int(input('Digite um número: '))
print('''escolha uma das bases de conversão:
[ 1 ] CONVERTER PARA BINÁRIO
[ 2 ] CONVERTER PARA OCTAL
[ 3 ] CONVERTER PARA HEXADECIMAL''')
opção = int(input('sua opção: '))
if opção == 1:
    print('o número {} convertido para binário e {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('o número {} convertido para octal é {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('o número {} convertido para hexadecimal é {}'.format(num,hex(num)[2:]))
else:
    print('informação INVÀLIDA.tente outro número')



