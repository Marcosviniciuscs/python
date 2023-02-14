n1 = int(input('\033[1;30mdigite um numero: '))
n2 = int(input('digite o segundo: \033[m'))
s = n1 + n2
print('\033[1;34ma soma entre {} e {} e igual {}: \033[m'.format(n1,n2,s))