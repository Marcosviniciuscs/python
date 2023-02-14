from datetime import date
ano = int(input('informe o ano? ou 0 para verificar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
