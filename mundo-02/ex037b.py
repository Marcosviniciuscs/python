print('{:=^20}'.format('CONVERSOR'))
num = int(input('Digite um numero inteiro: '))
print('''escolha uma da bases para converter:
[ 1 ] converter para binário 
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('sua opção: '))
if opção == 1 :
    print('convertido para binário é {}'.format(bin(num)[2:]))
elif opção == 2 :
    print('convertido para octal é {}'.format(oct(num)[2:]))
elif opção == 3 :
    print('convertido para hexadecimal é {}'.format(hex(num)[2:]))
else:
    print('Opção inválida!tente novamente.')


