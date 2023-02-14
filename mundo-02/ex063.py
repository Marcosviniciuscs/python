print('\033[1m-'*25)
print('Sequência de Fibonacci')
print('-'*25)
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2),end=' -> ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    cont = cont + 1
    print(t3,end=' -> ')
    t1 = t2
    t2 = t3
print('fim')