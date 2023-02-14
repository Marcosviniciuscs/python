from random import shuffle
n1 = str(input('\033[1;32m1º aluno: '))
n2 = str(input('2º aluno: '))
n3 = str(input('3º aluno: '))
n4 = str(input('4º aluno: \033[m'))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('\033[1;36ma ordem dos alunos será {}'.format(lista))

