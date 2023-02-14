from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10) , randint(0, 10) )
print('os numeros sorteados foram: ')
for n in numeros:
    print(n, end=' ')
maior = sorted(numeros)
print('\n','=-'* 20)
print('O maior número sorteado é {}'.format(maior[4]))
menor = sorted(numeros)
print('=-'* 20)
print(f'o Menor número sorteado é {menor[0]}')
print('=-'* 20)

