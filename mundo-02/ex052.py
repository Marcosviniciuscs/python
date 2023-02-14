cont = 0
num = int(input('digite um numero: '))
for c in range(1 , num +1):
    if num % c == 0:
        print('\033[1;33m{}\033[m'.format(c),end=" ")
        cont = cont + 1
    else:
        print('\033[1;31m{}\033[m'.format(c),end=' ')
print('\n\033[1mo número {} foi divisivel {} vezes.'.format(num,cont))
if cont == 2:
    print('o número {} È primo!'.format(num))
else:
    print('o numero {} Não é primo.\033[m'.format(num))
