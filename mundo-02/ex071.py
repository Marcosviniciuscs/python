print('='*25)
print('{:>18}'.format('BANCO ZARP'))
print('='*25)
print('CÈDULAS DISPONIVEIS: R$50 , R$20 , R$10 , R$1')
cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0
valor = int(input('quanto quer sacar? R$ '))
while valor >= 50:
    valor = valor - 50
    cont50 = cont50 + 1
while valor >= 20:
    valor = valor - 20
    cont20 = cont20 + 1
while valor >= 10:
    valor = valor - 10
    cont10 = cont10 + 1
while valor >= 1:
    valor = valor - 1
    cont1 = cont1 + 1
print(f'total de {cont50} cédulas de R$50')
print(f'total de {cont20} cédulas de R$20')
print(f'total de {cont10} cédulas de R$10')
print(f'total de {cont1} cédulas de R$1')
print('Volte sempre ao banco ZARP! tenha uma bom dia!')