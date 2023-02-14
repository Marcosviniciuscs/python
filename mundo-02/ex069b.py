pes = 0
masc = 0
fem = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF': #enquanto a informação da variavel 'sexo' nao estiver/não for 'MF'(validação de dados)
        sexo = str((input('sexo [M/F] '))).upper()[0]
    print('-'*20)
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar [S/N] ')).upper()
    if idade >= 18:
        pes = pes + 1
    if sexo in 'M':
        masc = masc + 1
    if sexo in 'F':
        if idade < 20:
            fem = fem + 1
    if 'N' in opção:
        break
print('*-'*25)
print(f'{pes} pessoas com mais de 18 anos')
print('{} homens foram cadastrados '.format(masc))
print(f'{fem} mulheres com menos de 20 anos foram registradas')
print('*-'*25)
