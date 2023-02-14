boletim = dict()
boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input(f'Média do {boletim["nome"]}: '))
if boletim['media'] < 5:
    boletim['Situação'] = 'REPROVADO'
elif boletim['media'] > 5 and boletim['media'] < 7:
    boletim['Situação'] = 'RECUPERAÇÃO'
elif boletim['media'] > 7:
    boletim['Situação'] = 'APROVADO'
print('=-'*15)
for k, v in boletim.items():
    print(f'  - {k} é igual a {v}')

