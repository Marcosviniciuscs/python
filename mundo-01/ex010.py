n1 = float(input('\033[1;36mquantos reais voce tem? '))
d = n1 / 5.30
e = n1 / 6.27
print('os seus R$ {:.2f} pode comprar :\033[m'.format(n1))
print('\033[1;32m{:.2f} dolares'.format(d))
print('{:.2f} euros'.format(e))
