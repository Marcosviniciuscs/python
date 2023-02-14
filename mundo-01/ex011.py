cores = {'blue':'\033[1:34m'}
print('{}{:=^20}'.format(cores['blue'],'area'))
alt = float(input('qual e a ALTURA ? '))
lar = float(input('qual e a LARGURA ? \033[m'))
area = alt * lar
c = area / 2
print('sua parede tem a dimensão de \033[1;31m{}x{}\033[m e possui uma \033[1;31márea {}m².\033[m\nvoce precisará de \033[1;31m{}litros de titas'.format(alt,lar,area,c))

