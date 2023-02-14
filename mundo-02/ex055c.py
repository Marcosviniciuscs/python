maior = 0
menor = 0
for p in range(1 ,6):
    peso = float(input('o peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('o maior peso lido é {}KG.'.format(maior))
print('o menor peso lido é {}KG.'.format(menor))
