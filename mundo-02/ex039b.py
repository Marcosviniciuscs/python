from datetime import date
#INTRODUÇÃO
print('''qual e o seu gênero:
[ 1 ] para masculino
[ 2 ] para feminino''')
sexo = int(input('sua opção: '))
if sexo == 1:
    print('{}sexo Masculino.{}'.format('\033[1;34m','\033[m'))
elif sexo == 2:
    print('{}sexo feminino.\nvocê nao precisa fazer o alistamento obrigatório.{}'.format('\033[1;31m','\033[m'))
    exit()
else:
    print('\033[1;33mtente novamente.\033[m')
#INICIO
nasc = int(input('ano de nascimento? '))
datapc = date.today().year
idade = datapc - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, datapc))
if idade < 18:
    saldo = 18 - idade
    print('ainda faltam {} anos para o seu alistamento.'.format(saldo))
    ano = datapc + saldo
    print('seu alistamento será em {}.'.format(ano))
elif idade == 18:
    print('o seu alistamento acontece neste ano.')
elif idade > 18:
    saldo = idade - 18
    print('você ja deveria ter se alistado há {} anos atrás.'.format(saldo))
    ano = datapc - saldo
    print('seu alistamento foi em {}'.format(ano))

