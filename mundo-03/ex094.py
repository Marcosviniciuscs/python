dados = dict()
cadastro = list()
soma = 0
while True:
    dados['Nome'] = str(input('Nome: '))

    dados['Sexo'] = str(input('Sexo [M/F] ')).upper()
    while dados['Sexo'] not in "MF":
        dados['Sexo'] = str(input('ERRO. Digite M ou F para continuar: ')).upper()

    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    cadastro.append(dados.copy())

    resp = str(input('Quer continuar? [S/N] ')).upper()
    while resp not in "SN":
        resp = str(input("Resposta inválida! informe S ou N: "))

    if resp in "Nn":
        break
print(f'A) Foram cadastradas {len(cadastro)} pessoas.')
media = soma / len(cadastro)
print(f'B) A media das idades das pessoas é {media:.2f} anos.')
print('C) As mulheres cadastradas foram:', end=' ')
for pessoa in cadastro:
    if pessoa['Sexo'] == "F":
        print(pessoa['Nome'])
print('D) Listas das pessoas que estão com a idade acima da média: ')
for pos, ind in enumerate(cadastro):
    if ind['Idade'] > media:
        for k, v in cadastro[pos].items():
            print(f'   {k} = {v};', end=' ')
        print()
print('<< Encerrado  >>')
