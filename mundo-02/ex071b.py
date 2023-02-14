print('='*25)
print('{:^25}'.format('BANCO ZARP'))
print('='*25)
print('Cédulas DISPONIVEIS: 1 , 10 , 20 , 50 ')
valor = int(input('quanto você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total = total - ced
        totced = totced + 1
    else:
        if totced > 0:
            print(f'total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*45)
print('tenha um bom dia! Volte sempre ão banco ZARP!')
