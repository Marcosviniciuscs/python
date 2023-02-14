print('-*'*15)
print('Sequência de Fibonacci')
print('-*'*15)
n = int(input('quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2),end=' -> ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    cont = cont + 1
    print(t3,end=' -> ')
    t1 = t2
    t2 = t3
    # 0   1  1  2   3   5   8   13
    #     t1 t2 t3
