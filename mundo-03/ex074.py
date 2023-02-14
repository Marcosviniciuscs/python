from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('os números sorteados foram: ')
for n in numeros:
    print(n,end=' ')
print('')
print(f'O maior números sorteados foi {max(numeros)}')
print(f'O menor número sorteado foi {min(numeros)}')
