from math import hypot
cores = {'yellow':'\033[1;33m',
         'red':'\033[1;31m',
         'blue2':'\033[1;32m',
         'clean':'\033[m'}
co = float(input('{}comprimento do cateto oposto: '.format(cores['yellow'])))
ad = float(input('comprimento do cateto adjacente: {}'.format(cores['clean'])))
conta = hypot(co , ad)
print('{}A hipotenusa desse triangulo retangulo equivale a{} {:.2f}'.format(cores['red'],cores['blue2'],conta))




