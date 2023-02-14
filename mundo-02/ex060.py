mult = 1
n1 = int(input('digite um numero: '))
print('{}!n ='.format(n1),end=" ")
for n in range(n1, 0, -1):
    print(n, end=' ')
    mult = mult * n
print( '= ', mult)
