from datetime import datetime
dados = dict()

dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['carteira'] = int(input('Número da ctps: '))
dados['idade'] = datetime.now().year - nasc

if dados['carteira'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (35 - (datetime.now().year - dados['contratação']))
print('-=' * 15)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
