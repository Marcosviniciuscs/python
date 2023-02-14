km = float(input('quantos KM foi percorrido na viagem? '))
print('voce esta preste a iniciar uma viagem de {} KM.'.format(km))
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print('o preço da passagem custará R${}'.format(preço))
