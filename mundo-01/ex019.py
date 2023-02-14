#import random
from random import choice
n1 = str(input('\033[1;32mnome do 1º aluno: '))
n2 = str(input('nome do 2º aluno: '))
n3 = str(input('nome do 3º aluno: '))
n4 = str(input('nome do 4º aluno: \033[m'))
lista = [n1,n2,n3,n4]
sorteio = choice(lista)
print('\033[1;7;34mo aluno escolhido foi o {}\033[m'.format(sorteio))
