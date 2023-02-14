from datetime import date
nasc = int(input('Ano de nascimento: '))
data = date.today().year
idade = data - nasc
print('voce tem {} anos.'.format(idade))
if idade <= 9:
    print('CATEGORIA: MIRIM.')
elif idade <= 14:
    print('CATEGORIA: INFANTIL.')
elif idade <= 19:
    print('CATEGORIA: JÙNIOR.')
elif idade <= 25:
    print('CATEGORIA: SÊNIOR.')
else:
    print('CATEGORIA: MASTER.')

