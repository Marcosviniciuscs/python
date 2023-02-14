print('{:=^19}'.format(' Gerador de PA '))
primeiro = int(input('primeiro termo: '))
razão = int(input('razão: '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        an = primeiro + (cont - 1) * razão
        cont = cont + 1
        print('\033[1m',an,end='\033[1;34m -> \033[m')
    print('\033[1mpausa\033[m')
    mais = int(input('quer mais termos? '))
print('foram contabilizados {} termos no total.'.format(cont - 1))
