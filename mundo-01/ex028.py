from random import randint
from time import sleep
cmp = randint(0,5)
print('--=--='*9)
print('pensei em um número entre 0 e 5 .tente adivinhar...')
print('--=--='*9)
pc = input('tente acertar o numero: ')
if pc.isspace() == True:
    print('digite apenas números!')
    exit()
if pc.isalpha() == True:
    print('digite apenas os numeros mencionados.')
    exit()
pc1 = int(pc)
if pc1 > 5:
    print('informe um valor menor ou igual a 5.')
    exit()
print('Processando...')
sleep(2)
if cmp == pc1:
    print('\nparabéns voce ganhou!')
else:
    print('eu escolhi o número {} e voce {}\n'.format(cmp,pc1))
    print('eu ganhei!urruuu !\ntente novamente.')
