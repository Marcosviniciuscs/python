num = int(input('informe um número: '))
print('analizando o numero... {}'.format(num))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print('UNIDADE:{}'.format(u))
print('DEZENA: {}'.format(d))
print('CENTENA: {}'.format(c))
print('MILHAR: {}'.format(m))







