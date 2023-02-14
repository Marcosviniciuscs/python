n = int(input('digite um número para calcular o fatorial: '))
f = 1
c = n
print('Calculando {}! = '.format(n),end='')
while c > 0:
    print('{}'.format(c),end=' ')
    print('x' if c > 1 else '=',end=' ')
    f = f * c
    c = c - 1
print('{}'.format(f))

