num = (int(input('digite um número: ')),
       int(input('digite o segundo: ')),
       int(input('digite mais um: ')),
       int(input('digite o ultimo: ')))
print(f'o numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o primeiro 3 foi digitado na posição {num.index(3) + 1}')
else:
    print('o 3 nao foi digitado')
print('os valores pares digitados foram: ')
for n in num:# a variavel 'n' lê cada elemento da tupla
    if n % 2 == 0:
        print(n , end=',')


