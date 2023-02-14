from time import sleep
pes = 0
h = 0
f = 0
while True:
    print('-'*20)
    print('\033[1mCADASTRE UMA PESSOA\033[m')
    print('-'*20)
    idade = int(input('informe a sua idade: '))
    sexo = str(input('Qual é o seu sexo: ')).strip().upper()[0]
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar [s/n] ')).strip().upper()[0]
    if idade >= 18:
        pes = pes + 1
    if sexo == 'M':
        h = h + 1
    if sexo == 'F':
        if idade < 20:
            f = f + 1
    if opção == 'N':
        break
print('\033[1m*-\033[m'*25)
print(f'foram contabilizados {pes} pessoas com mais de 18 anos ')
print(f'{h} homens foram registrados.')
print(f'{f} mulheres com menos de 20 anos foram registrados')
print('*-'*25)
print('PROGRAMA FINALIZADO...')
sleep(1)
print('='*20)
