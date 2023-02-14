cores = {'clean':'\033[m',
         'blue':'\033[1;34m',
         'red':'\033[1;31m',
         'yellow':'\033[1;33m',
         'white':'\033[1;30m'}
n1 = input('\033[1;30mdigite algo: \033[m')
print('{}tipo primitivo: {}'.format(cores['red'],type(n1)))
print('{}E um número? {}'.format(cores['blue'],n1.isnumeric()))
print('{}E alfanumerico? {}{}'.format(cores['yellow'],n1.isalnum(),cores['clean']))
print('{}E alfabetico? {}'.format(cores['blue'],n1.isalpha()))
print('{}esta escrito em letras maiusculas? {}'.format(cores['yellow'],n1.isupper()))
print('{}esta escrito em letras minusculas? {}'.format(cores['blue'],n1.islower()))
print('{}so tem espaços? {}'.format(cores['yellow'],n1.isspace()))
print('{}esta capitalizada? {}'.format(cores['blue'],n1.istitle()))


