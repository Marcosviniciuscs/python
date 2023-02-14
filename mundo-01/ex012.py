cores = {'limpa':'\033[m',
         'blue':'\033[1;34m',
         'red':'\033[1;31m',
         'blue2':'\033[1;36m'}
pr = float(input('\033[1;36mqual e o preço do produto? '))
por = int(input('quantos porcentos de desconto? \033[m'))
c1 = pr -(pr * por)/100
print('\n{}O produto esta com {}% de desconto!\n{}Custará apenas {} reais.'.format(cores['red'],por,cores['blue'],c1))

